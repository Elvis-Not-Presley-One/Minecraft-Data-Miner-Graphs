import csv
import sqlite3
import pandas as pd
import dask.dataframe as dd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL.ImageOps import scale
from docutils.nodes import title
from docutils.utils.punctuation_chars import delimiters
from holoviews.plotting.bokeh.styles import marker
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from sympy import rotations
from IPython.display import display
from matplotlib.patches import ConnectionPatch
import plotly.express as px
import plotly.graph_objs as go
from xarray.util.generate_ops import inplace

from ThreeDGraphs import ThreeDGraphs
from TwoDGraphs import TwoDGraphs
from Util import Util
from Biomes import Biomes
import json
from charset_normalizer import from_path
from tabulate import tabulate


def getBannerData(filename):
    """
    The getBannerData() function obtains and creates a list for all cols in the csv file

    :param filename: The filename you want to look for
    :return: lists of data i.e(x, y, z...)
    """

    try:
        pd.set_option('display.max_rows', None)
        df = pd.read_csv(filename, on_bad_lines='skip', header=None, dtype='string')
        print(df.info())
        print(df.head())
        print(df.head(10))

        col_pat = []
        for _, row in df.iterrows():
            row_col_pat = []

            for col in range(5, len(row)):
                cell = str(row[col])
                if cell == '<NA>' or cell == 'nan':
                    continue
                else:
                    row_col_pat.append(cell)

            col_pat.append(" ".join(row_col_pat))

        banner_x_cord = df[0]
        banner_y_cord = df[1]
        banner_z_cord = df[2]
        banner_names = df[3].fillna('No-Name')

        cleaned_data = {
            "x": banner_x_cord,
            "y": banner_y_cord,
            "z": banner_z_cord,
            "name": banner_names,
            "Color and Pattern": col_pat,
        }

        new_df = pd.DataFrame(cleaned_data, dtype='string')
        new_df.to_html("Cleaned Banner Data spawn.html")

        x = new_df['x']
        y = new_df['y']
        z = new_df['z']
        name = new_df['name']
        color_and_Pattern = new_df['Color and Pattern']

        new_df.info()

    except Exception as e:
        print(f"Failed to Create DataFrame {e}")
        return None, None, None, None, None, None

    return banner_x_cord.astype(int), banner_y_cord.astype(int), banner_z_cord.astype(int), name, color_and_Pattern, name.unique()


def get_Sign_data(filename):
    # *NOTE Pandas is fucking up x y z cords
    # nvm found the issue

    # create pandas dataframe
    try:
        df = pd.read_csv(filename, header= None, on_bad_lines='skip', delimiter=',', dtype='string')
        print(df.head(10))  # Preview first few rows
        df.info()
        df.astype(str)

        print('Finished loading in first data set\nstarting String man')
        # took too many fucking hrs to figure this out
        df.replace('{"type":"ListTag"', '', inplace=True, regex=True)
        df.replace(r'\\"text\\":\\"\\\"\}"', '', inplace=True, regex=True)
        df.replace('value:{"type":"StringTag"', '', inplace=True, regex=True)
        df.replace(r'\\\\""', '', inplace=True, regex=True)
        df.replace(r']\}\}', '', inplace=True, regex=True)
        df.replace(r'list:\\', '', inplace=True, regex=True)
        df.replace(r'{\\extra\\":', '', inplace=True, regex=True)
        df.replace(r'[\\]', '', inplace=True, regex=True)
        df.replace('list:[""""]', '', inplace=True, regex=True)
        df.replace(r'{\"type":"CompoundTag"', '', inplace=True, regex=True)
        df.replace(r'{\"type":"ByteTag"', '', inplace=True, regex=True)
        df.replace(r'{\"type":"StringTag"', '', inplace=True, regex=True)
        df.replace(r'}\}\}', '', inplace=True, regex=True)
        df.replace(r'value:{\"messages":', '', inplace=True, regex=True)
        df.replace(r'list:[\""""]', '', inplace=True, regex=True)
        df.replace(r'}', '', inplace=True, regex=True)
        df.replace(r'list:[\"{\"extra":]', '', inplace=True, regex=True)
        df.replace('list:', '', inplace=True, regex=True)
        df.replace('""""', '', inplace=True, regex=True)
        df.replace(r'\[', '', inplace=True, regex=True)
        df.replace(r'\]', '', inplace=True, regex=True)
        df.replace(r'"{\"extra":', '', inplace=True, regex=True)

        print('Done With String man\nremove rows')
        # remove the last rows 32 onward since it repeats data and does not have anything of meaning
        df = df.iloc[:, :32]

        # Note need to clean up the file even more
        # remove all white space ect.

        # get x y z from the original data frame
        x_cord = df[0]
        y_cord = df[1]
        z_cord = df[2]

        print('Start cleaning up empty row ')
        glow_ink = []
        messages = []
        ink_color= []
        for _, row in df.iterrows():

            row_messages = []
            glow_ink_row = []
            ink_color_row = []
            seen_messages = set()

            for col in range(3, len(row)):
                cell = str(row[col])

                # if the cell does not start with any of the other cells it must be a msg, get the info
                if (not cell.startswith("has_glowing_text:") and not cell.startswith("color:")
                        and not cell.startswith('value:') and not cell.startswith('<NA>') and cell != 'nan'):
                    cleaned_message = cell.strip('"').strip()
                    if cleaned_message not in seen_messages:
                        row_messages.append(cleaned_message)
                        seen_messages.add(cleaned_message)

                # get the glow ink text 0 false 1 for true
                if cell.startswith("has_glowing_text:"):
                    combined_glow_ink = cell
                    if col + 1 < len(row):
                        next_cell = str(row[col + 1]).strip()
                        if next_cell.startswith("value:"):
                            combined_glow_ink += f" {next_cell}"
                    glow_ink_row.append(combined_glow_ink)

                # get the colors of the signs
                if cell.startswith("color:"):
                    combined_color = cell
                    if col + 1 < len(row):
                        next_cell = str(row[col + 1]).strip()
                        if next_cell.startswith("value:"):
                            combined_color += f" {next_cell}"
                    ink_color_row.append(combined_color)

            # combine and remove "" from the cells into one multi dem array
            ink_color.append(" ".join(ink_color_row))
            glow_ink.append(" ".join(glow_ink_row))
            messages.append(" ".join(row_messages))



        #creating a dic for the new data frame
        cleaned_data = {
            "x": x_cord,
            "y": y_cord,
            "z": z_cord,
            "mgs": messages,
            "Glow Ink": glow_ink,
            "Sign Color": ink_color
        }
        print('Create new dataframe')
        # creates a new data frame to make everything nice and org
        new_df = pd.DataFrame(cleaned_data, dtype='string')
        #new_df.to_html("Cleaned Sign Data spawn.html")


        x = new_df['x']
        y = new_df['y']
        z = new_df['z']
        msg = new_df['mgs']
        glow = new_df['Glow Ink']
        color = new_df['Sign Color']

        new_df.info()
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None, None, None, None

    return x.astype(int), y.astype(int), z.astype(int), msg, glow, color, msg.unique(), glow.unique(), color.unique()


def main():
    """
    This is the main
    """

    filename_banners = 'FilesBanners.csv'
    filename_signs = 'FilesSignsV2.csv'
    filename_Biome = 'D:/FilesBiomes.csv'
    filename_test = 'test.csv'
    spawn_banners = 'FileslampBanners.csv'
    spawn_Signs = 'FileslampSignsV2.csv'


    #sign_x, sign_y, sign_z, msg, glow, sign_color, unique_msg, unique_glow, unique_color = get_Sign_data(filename_signs)

    #sign_utils = Util(filename_signs, msg)

    #sign_data, sign_keys = sign_utils.unique_word_counter()

    #sign_threeD_Graph = ThreeDGraphs(sign_x, sign_y, sign_z, msg, glow, sign_color, unique_msg, unique_glow, unique_color)

    #sign_threeD_Graph.scatter_Plot()
    #sign_threeD_Graph.add_Drop_Downs()
    #sign_threeD_Graph.show()
    #sign_threeD_Graph.html('3d_Sign_plot.html')

    title = 'All Signs In 2b End 25k'
    yLabel = 'Amount of Signs'
    xLabel = 'Name of Sign'
    overall = ['The Rest', 'Empty Sign']

    #signs_2dGraph = TwoDGraphs(sign_data, sign_keys)
    #signs_2dGraph.Create_Bar_Charts(yLabel,xLabel,title)
    #signs_2dGraph.create_Percent_Pie_Chart(overall)


    """
    =====================
    Spawn OW
    ====================
    """

    sign_x, sign_y, sign_z, msg, glow, sign_color, unique_msg, unique_glow, unique_color = get_Sign_data(spawn_Signs)

    sign_utils = Util(filename_signs, msg)

    sign_data, sign_keys = sign_utils.unique_word_counter()

    #sign_threeD_Graph = ThreeDGraphs(sign_x, sign_y, sign_z, msg, glow, sign_color, unique_msg, large_DataSet=True)

   # sign_threeD_Graph.scatter_Plot()
   # sign_threeD_Graph.show("SignsOW.html")

    title = 'All Signs In 2b Spawn OW 10k'
    yLabel = 'Amount of Signs'
    xLabel = 'Name of Sign'
    overall = ['Cody Signs', 'Empty Sign']

    #signs_2dGraph = TwoDGraphs(sign_data, sign_keys)
    #signs_2dGraph.Create_Bar_Charts(yLabel,xLabel,title)
    #signs_2dGraph.create_Percent_Pie_Chart(overall)


    (banner_x_list, banner_y_list, banner_z_list, banner_names_list,
     banner_color_list, banners_unique_names_only) = getBannerData(spawn_banners)

    utils = Util(filename_banners, banner_names_list)
    banner_data, banner_keys = utils.unique_word_counter()

    #twoDGraph = TwoDGraphs(banner_data, banner_keys)

    #twoDGraph.Create_Bar_Charts('Amount of Banner', 'Name of Banner', 'All Banner in End')
    #twoDGraph.create_Percent_Pie_Chart([])

    sign_threeD_Graph = ThreeDGraphs(banner_x_list, banner_y_list, banner_z_list, banner_names_list, banner_color_list, unique_names=banners_unique_names_only,
                                     large_DataSet=False)

    sign_threeD_Graph.scatter_Plot()
    sign_threeD_Graph.show("BannersOW1.2.html")

    """
    =================================
    End Below
    =================================
    """

    (banner_x_list, banner_y_list, banner_z_list, banner_names_list,
     banner_color_and_pat_list, banners_unique_names_only) = getBannerData(filename_banners)

    utils = Util(filename_banners, banner_names_list)
    banner_data, banner_keys = utils.unique_word_counter()

    twoDGraph = TwoDGraphs(banner_data, banner_keys)

    twoDGraph.Create_Bar_Charts('Amount of Banner','Name of Banner', 'All Banner in End')
    twoDGraph.create_Percent_Pie_Chart(['Nan','PHr Thomas'])



    
if __name__ == "__main__":
    main()

