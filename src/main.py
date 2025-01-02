import csv

import pandas as pd
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
from ThreeDGraphs import ThreeDGraphs
from TwoDGraphs import TwoDGraphs
from Util import Util
import json
from charset_normalizer import from_path
from tabulate import tabulate


def getBannerData(filename):
    """
    The getBannerData() function obtains and creates a list for all cols in the csv file

    :param filename: The filename you want to look for
    :return: lists of data i.e(x, y, z...)
    """

    pd.set_option('display.max_rows', None)
    data = pd.read_csv(filename, on_bad_lines='skip')

    # user needs to put in own col info in the [] (Needs exact spacing!)
    # in the future just add a header of use Header=False
    banner_x_cord = data['-514'].array
    banner_y_cord = data['140'].array
    banner_z_cord = data['-13414'].array
    banner_names = data['Unnamed: 3'].fillna('No-Name').array
    banner_color = data['White'].array
    banner_pat = data['Top Triangle '].array


    return banner_x_cord, banner_y_cord, banner_z_cord, banner_names, banner_color, banner_pat, banner_names.unique()



def get_Sign_data(filename):
    # *NOTE Pandas is fucking up x y z cords
    # nvm found the issue

    # create pandas dataframe
    try:
        df = pd.read_csv(filename, header= None, on_bad_lines='skip', delimiter=',', dtype='string')
        print(df.head(10))  # Preview first few rows
        df.info()
        df.astype(str)


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

        """
        msg_list = []

        # Get all the msgs from the signs
        for k in range(len(df[0].array)):
            single_msg_list = []
            for i in range(5, 10, 2):
                if i == 9:
                    i += 1
                single_msg_list.append(df.iloc[k, i])
            msg_list.append(single_msg_list)
        """


        # NOTE 32 col can remove everything from there
        # Note need to clean up the file even more
        # remove all white space ect.

        x_cord = df[0]
        y_cord = df[1]
        z_cord = df[2]

        df.to_html('asss.html')

    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    This is the main
    """
    filename_banners = 'FilesBanners.csv'
    filename_signs = 'FilesSignsV2.csv'


    get_Sign_data(filename_signs)
    """
    (banner_x_list, banner_y_list, banner_z_list, banner_names_list,
     banner_color_list, banner_pat_list, banners_unique_names_only) = getBannerData(filename_banners)

    utils = Util(filename_banners, banner_names_list)
    banner_data, banner_keys = utils.unique_word_counter()

    twoDGraph = TwoDGraphs(banner_data, banner_keys)

    twoDGraph.Create_Bar_Charts()
    twoDGraph.create_Percent_Pie_Chart()

"""
if __name__ == "__main__":
    main()

