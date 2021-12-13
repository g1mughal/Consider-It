"""
@Author: Qadir Mughal

NOTE: if the file is in GBs then pandas in good library
but if you exceed then you need to think about other
solution.
"""
import pandas as pd
import os.path


class FileHandler:
    def __init__(self, filename=None, separator=','):
        self.filename = filename
        self.separator = separator

    def file_reading_by_dataframe(self):
        """
        Read the file into pandas dataframe
        :return:
        """
        try:
            if os.path.isfile(self.filename):
                return pd.read_csv(self.filename, sep=self.separator)
            else:
                raise Exception("FileHandler: file does not exist")

        except FileNotFoundError as e:
            print("FileHandler: error in file opening.")
            print(e)
