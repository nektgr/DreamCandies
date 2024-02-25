import unittest
import os
from entities.abstract_file import CSVDataFile

class Test_abstaction_file(unittest.TestCase):
        
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_file_path = 'test_file2.csv'
        with open(self.test_file_path, 'w', encoding='utf-8') as test_file:
            test_file.write(" “CUSTOMER_CODE”,“FIRSTNAME”,“LASTNAME” \n")
            test_file.write(" “CUST0000010231”,“Maria”,“Alba” ")

    def tearDown(self):
        # Clean up: Delete the temporary test file
        os.remove(self.test_file_path)

    def test_read_file_setup_teardown(self):
        # Create an instance of CSVDataFile and call read_file
        csv_file = CSVDataFile(self.test_file_path)
        csv_file.read_file()

        # Assert that the fields and data have been populated correctly
        expected_fields = ['CUSTOMER_CODE','FIRSTNAME','LASTNAME']
        expected_data = [['CUST0000010231','Maria','Alba']]

        self.assertEqual(csv_file.fields, expected_fields)
        self.assertEqual(csv_file.data, expected_data)


