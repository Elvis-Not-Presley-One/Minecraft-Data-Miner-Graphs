import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from Util import Util

class TwoDGraphs:

    def __init__(self, list_of_data, keys):
        """
        this is the con for the TwoDGraphs class

        :param list_of_data: a list of values int/float
        :param keys: a list of str of keys from a dic
        """

        self.__data = list_of_data
        self.__keys = keys

    def create_Percent_Pie_Chart(self):
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
        overall_labels = ['No-Name', 'PRThomass Banner ', 'Other Named Banners']
        explode = [0.1, 0.0, 0.0]
        angle = -180 * overall_ratios[0]
        wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                             labels=overall_labels, explode=explode)

        plt.show()

    def Create_Bar_Charts(self):
        """
        the Create_Bar_Charts function creates Two bar chart
        :return:
        dic_keys: the keys from the dic in a list of str
        self.__dic_data: a list of values from the dic data list
        dic_values: creates a list from the dic values
        """
        dic_keys = [str(key) for key in self.__keys]
        dic_values = list(self.__data)

        print(dic_keys)
        print(dic_values)
        # For log Scaled Data
        try:
            colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan']

            plt.bar(dic_keys, dic_values, color=colors[:len(dic_keys)])
            plt.yscale('log')
            plt.ylabel('Amount of Banners in Log Scale')
            plt.xlabel('Different Banners')
            plt.title('All of 2b2t"s Banners in 25k 25k end')
            plt.xticks(rotation=45, ha='right', size=5)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"Error Creating scaled bar graph {e}")

        try:
            # For non log scaled data bar chart
            plt.bar(dic_keys, dic_values, color=colors[:len(dic_keys)])
            plt.ylabel('Amount of Banners in With No Scale')
            plt.xlabel('Different Banners')
            plt.title('All of 2b2t"s Banners in 25k 25k end')
            plt.xticks(rotation=45, ha='right', size=5)
            plt.tight_layout()
            plt.show()

            dicts = {'Banner Name': dic_keys,
                     'Amount of Banners': self.__data}

            df = pd.DataFrame(dicts)
            display(df)
        except Exception as e:
            raise RuntimeError(f"Error in creating non-log bar graph {e}")

        return dic_keys, self.__data, dic_values

