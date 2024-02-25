import unittest
import os
from unittest.mock import patch, mock_open
from entities.abstract_file import CSVDataFile
from initialization.files_operations import list_files_in_folder, list_files_with_customer_code, filter_data_based_on_keyvalue, filter_data_based_on_customercode

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources or configurations
        self.folder_path = 'test_folder'
        self.exclude_file = 'exclude.txt'
        self.files_list = ['file1.csv', 'file2.csv', 'file3.txt']
        self.input_folder = 'test_input'
        self.matched_file_path = 'test_folder/matched_file.csv'
        self.unmatched_file_path = 'test_folder/unmatched_file.csv'
        self.keyvalue = 'KEY'
        self.output_folder = 'test_output'
        self.prefix = 'TEST_'
        self.desired_customers = [['CODE1', 'Name1'], ['CODE2', 'Name2']]
        self.flattened_desired_customers = ['CODE1', 'Name1', 'CODE2', 'Name2']

    def tearDown(self):
        # Clean up any resources created during testing
        pass

    #write tests as needed

if __name__ == '__main__':
    unittest.main()
