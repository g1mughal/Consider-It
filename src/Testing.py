"""
@Author: Qadir Mughal

Different testcase will be implemented here

"""
import os
import sys

import unittest2 as unittest2

from FileHandler import FileHandler

os.chdir(sys.path[0])


class TestCases(unittest2.TestCase):

    def test_file(self):
        file = FileHandler('../csv/project.csv', ';')
        data = file.file_reading_by_dataframe()
        self.assertGreater(len(data), 0)


if __name__ == "__main__":
    unittest2.main()
