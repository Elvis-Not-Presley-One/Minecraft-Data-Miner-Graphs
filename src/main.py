import csv

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL.ImageOps import scale
from docutils.nodes import title
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


def getBannerData(filename):
    """
    The getBannerData() function obtains and creates a list for all cols in the csv file

    :param filename: The filename you want to look for
    :return: lists of data i.e(x, y, z...)
    """

    pd.set_option('display.max_rows', None)
    data = pd.read_csv(filename, on_bad_lines='skip')

    # user needs to put in own col info in the [] (Needs exact spacing!)
    banner_x_cord = data['-514'].array
    banner_y_cord = data['140'].array
    banner_z_cord = data['-13414'].array
    banner_names = data['Unnamed: 3'].fillna('No-Name').array
    banner_color = data['White'].array
    banner_pat = data['Top Triangle '].array


    return banner_x_cord, banner_y_cord, banner_z_cord, banner_names, banner_color, banner_pat, banner_names.unique()



def get_Sign_data(filename):
    # *NOTE Pandas is fucking up x y z cords
    try:
        df = pd.read_csv(filename, header= None, on_bad_lines='skip', delimiter=',')
        print(df.head(10))  # Preview first few rows
        df.info()
        print(df.iloc[10])
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

