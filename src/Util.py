import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

class Util:
    """
    The Util class is for the util functions

    Author: Elvis
    """

    def __init__(self, filename = '', msg_List = [], data_list = []):
        """
        This is the con for the Util class

        :param filename: a str of a filename
        :param msg_List: a list of msgs/names
        :param data_Value_List: a list of any type of int/float value
        """

        self.__filename = filename
        self.__list = msg_List
        self.__data = data_list

    def get_Total(self):
        """
        the get_Total function obtains the total vlaue from an int/float list
        :return: the total sum *NOTE int/float
        """

        #finds the sum, could use sum() to clean it up, but thats not how I was tought py
        sums = 0
        for item in self.__data:
            sums += item
        return sums

    def unique_word_counter(self):
        """
        the unique_word_counter creates an dictionary of all unique words and how many times
        the word was said then separates them into its list of keys and values
        :return: a list of values and keys
        """

        unique_words = {}
        
        #NOTE this only prints the msg not the words in the msg
        for words in self.__list:
            if words in unique_words:
                unique_words[words] += 1
            else:
                unique_words[words] = 1
        print('done')


        # outputs the keys and values associated with them
        return list(unique_words.values()), list(unique_words.keys())

    def unique_word_dic(self, csvname, wordcloud=False):
        """
        the unique_word_counter creates an dictionary of all unique words and how many times
        the word was said then separates them into its list of keys and values
        :return: a list of values and keys
        """

        unique_words = {}
        msg = " ".join(self.__list).split()
        # NOTE this only prints the msg not the words in the msg
        for words in msg:
            if words in unique_words:
                unique_words[words] += 1
            else:
                unique_words[words] = 1
        print('done')
        print(unique_words)

        with open(csvname, mode='w', newline='', encoding='Latin-1') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Count'])  # CSV headers

            for word, count in unique_words.items():
                writer.writerow([word, count])

        print('CSV file created successfully')

        if not wordcloud:
            plt.subplots(figsize=(8, 8))

            wordcloud = WordCloud(
                background_color='white',
                width=512,
                height=384

            ).generate_from_frequencies(unique_words)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.savefig('Plotly-World_Cloud.png')
            plt.show()

        # outputs the keys and values associated with them
        return list(unique_words.values()), list(unique_words.keys())

    def display_Info(self):
        """
        the display_Info function displays useful info to the console
        :return: Nothing but useful print statements
        """

        # basic info you might want to look at before doing stuff to the df
        pd.set_option('display.max_rows', None)
        data = pd.read_csv(self.__filename, on_bad_lines='skip')
        print(data.head())
        print(data.tail())
        print(data.shape)
        print(data.info())