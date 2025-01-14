import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from Util import Util
import plotly.graph_objs as go



class TwoDGraphs:

    def __init__(self, list_of_data, keys, x_cord=None, y_cord=None, name=None, unique_name=None):
        """
        this is the con for the TwoDGraphs class

        :param list_of_data: a list of values int/float
        :param keys: a list of str of keys from a dic
        """

        self.__data = list_of_data
        self.__keys = keys
        self.__x = x_cord
        self.__y = y_cord
        self.__name = name
        self.__unique = unique_name

        if self.__x is not None:
            self.__hover_text = [
                (f"<br>X:{self.__x[i]}<br>Z: {self.__y[i]}<br>Biome:,"
                 f" {self.__name[i]}")
                for i in range(len(self.__x))
            ]

        self.__fig = go.Figure()

    def create_Percent_Pie_Chart(self, overall):
        """
        the create_Percent_Pie_Chart creates a percent pie chart
        :return: Nothing
        """

        #create a util obk
        utils = Util('', self.__keys, self.__data)
        total = utils.get_Total()

        percent_list = []
        non_big_percent = []
        sums = 0

        #find the percent of each banner
        for item in self.__data:
            percent = (item / total) * 100
            if percent >= 10.00:
                percent_list.append(percent)
            else:
                non_big_percent.append(percent)
                sums += percent

        percent_list.append(sums)

        # make fig obj's
        fig, ax1 = plt.subplots()
        fig.subplots_adjust(wspace=0)

        # pie chart params
        overall_ratios = percent_list
        overall_labels = overall
        angle = -180 * overall_ratios[0]
        wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle, #labels=overall_labels
                            )

        plt.show()

    def Create_non_log_bar(self, yLabel, xLabel, title):
        dic_keys = [str(key) for key in self.__keys]
        dic_values = list(self.__data)

        colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan']

        try:
            # For non log scaled data bar chart
            plt.bar(dic_keys, dic_values, color=colors[:len(dic_keys)])
            plt.ylabel(yLabel)
            plt.xlabel(xLabel)
            plt.title(title)
            plt.xticks(rotation=45, ha='right', size=5)
            plt.tight_layout()
            plt.show()


        except Exception as e:
            raise RuntimeError(f"Error in creating non-log bar graph {e}")

        return dic_keys, self.__data, dic_values

    def Create_Bar_Charts(self, yLabel, xLabel, title):
        """
        the Create_Bar_Charts function creates Two bar chart
        :return:
        dic_keys: the keys from the dic in a list of str
        self.__dic_data: a list of values from the dic data list
        dic_values: creates a list from the dic values
        """
        dic_keys = [str(key) for key in self.__keys]
        dic_values = list(self.__data)

        dicts = {'Sign Name': dic_keys,
                 'Amount of Signs': self.__data}

        df = pd.DataFrame(dicts)
        df.to_markdown()
        df.to_csv('OW Banner Dic.csv')
        display(df)

        # For log Scaled Data
        try:
            colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan']

            plt.bar(dic_keys, dic_values, color=colors[:len(dic_keys)])
            plt.yscale('log')
            plt.ylabel(yLabel)
            plt.xlabel(xLabel)
            plt.title(title)
            plt.xticks(rotation=45, ha='right', size=5)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"Error Creating scaled bar graph {e}")



        return dic_keys, self.__data, dic_values

    def twoD_Scatter_Plot(self):
        try:
            x = self.__x
            z = self.__y

            # creates title marker type color and text with a scale
            self.__fig = go.Figure(data=[go.Scatter(
                x=x,
                z=z,
                mode='markers',
                text=self.__hover_text,
                hoverinfo="text",
                marker=dict(
                    size=8,
                    colorscale='rdbu',
                    opacity=0.8,


                )
            )])
        except Exception as e:
            raise RuntimeError(f"Error creating the first plot: {e}")

    def add_drop_downs(self):
        try:
            filter_buttons = [
                dict(
                    args=[{

                        'x': [[self.__x[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]],
                        'z': [[self.__y[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]],
                        'text': [[self.__hover_text[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]]
                    }],

                    label=unique_name,
                    method="update"
                )
                    for unique_name in self.__unique
            ]

            filter_buttons.insert(0, dict(
                args=[{
                    'x': [self.__x],
                    'z': [self.__y],
                    'text': [self.__hover_text]
                }],
                label='all',
                method='update'

            ))



            # create a drop down with the button name and what it does
            buttons_types = [

                dict(
                    args=['type', 'scatter2d'],
                    label='2d-Plot',
                    method='restyle'
                ),
                dict(
                    args=['type', 'heatmap'],
                    label='heatmap',
                    method='restyle'
                )

            ]

            # makes buttons do shit, and can style them here
            self.__fig.update_layout(
                template='plotly_dark',
                updatemenus=[
                    dict(
                        buttons=buttons_types,
                        direction='down',
                        pad={'r': 10, 't': 10},
                        showactive=True,
                        x=0.1,
                        xanchor='left',
                        y=1.15,
                        yanchor='top',
                        name='Plot Type: '
                    ),
                    dict(
                        buttons=filter_buttons,
                        direction='down',
                        pad={'r': 10, 't': 10},
                        showactive=True,
                        x=0.5,
                        xanchor='left',
                        y=1.15,
                        yanchor='top',
                        name='Filters'

                    ),

                ],

                # make text for the buttons to the side of them
                annotations=[
                    dict(text="Plot Types:", showarrow=False,
                         x=0.024, y=1.13, yref="paper", align="left"),
                    dict(text='Filters:', showarrow=False,
                         x=0.455, y=1.13, yref='paper', align='left')
                ],
                scene=dict(
                    xaxis_title='X Axis',
                    zaxis_title='z Axis',
                ),
                width=1200,
                height=800,
                margin=dict(r=60, l=60, b=60, t=60)
            )
        except Exception as e:
            raise RuntimeError(f"Error with adding dropdowns: {e}" )

    def show(self):
        self.__fig.show()

    def html(self, name_of_file):

        try:
            self.__fig.write_html(name_of_file)
        except Exception as e:
            raise IOError(f"Error Saving as Html '{name_of_file}'{e}")