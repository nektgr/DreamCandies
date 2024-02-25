import unittest
import os
from entities.abstract_file import CSVDataFile
from initialization.files_operations import filter_data_based_on_customercode

class Test_Scenario_customercode(unittest.TestCase):
    """
    Test cases for the filter_data_based_on_customercode function.

    This class contains unit tests to ensure that the data filtering based on customer codes
    is working correctly for the provided CSV files.

    Test scenarios include reading files, filtering data based on customer codes, and verifying
    the correctness of the filtered output.

    Note: The CSV files are created and removed during the setup and teardown phases to ensure
    isolation and cleanliness of the test environment.

    Usage:
    python -m unittest <name_of_this_file.py>
    """
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_file_path = 'CUSTOMER.csv'
        with open(self.test_file_path, 'w', encoding='utf-8') as test_file:
            test_file.write(" “CUSTOMER_CODE”,“FIRSTNAME”,“LASTNAME” \n")
            test_file.write(" “CUST0000010231”,“Maria”,“Alba” \n")
            test_file.write(" “CUST0000010232”,“John”,“Dhoe” \n")
            test_file.write(" “CUST0000010233”,“Carolina”,“Herera” \n")
            test_file.write(" “CUST0000010234”,“Nick”,“Adersen” \n")
        self.test_file_path2 = 'CUSTOMER_SAMPLE.csv'
        with open(self.test_file_path2, 'w', encoding='utf-8') as test_file:
            test_file.write(" “CUSTOMER_CODE” \n")
            test_file.write(" “CUST0000010231”\n")
            test_file.write(" “CUST0000010232”\n")
            test_file.write(" “CUST0000010233”\n")
        self.test_file_path3 = 'INVOICE.csv'
        with open(self.test_file_path3, 'w', encoding='utf-8') as test_file:
            test_file.write(" “CUSTOMER_CODE”,“INVOICE_CODE”,“AMOUNT”,“DATE” \n")
            test_file.write(" “CUST0000010231”,“IN0000001”,“105.50”,“01-Jan-2016” \n")
            test_file.write(" “CUST0000010235”,“IN0000002”,“115.50”,“01-Jan-2016” \n")
            test_file.write(" “CUST0000010233”,“IN0000003”,“35.50”,“01-Jan-2016” \n")
            test_file.write(" “CUST0000010231”,“IN0000004”,“25.50”,“01-Jan-2016” \n")
        self.test_file_path4 = 'INVOICE_ITEM.csv'
        with open(self.test_file_path4, 'w', encoding='utf-8') as test_file:
            test_file.write(" “INVOICE_CODE”,“ITEM_CODE”,“AMOUNT”,“QUANTITY” \n")
            test_file.write(" “IN0000001”,“MEIJI”,“75.60”,“100” \n")
            test_file.write(" “IN0000001”,“POCKY”,“10.40”,“250” \n")
            test_file.write(" “IN0000001”,“PUCCHO”,“19.50”,“40” \n")
            test_file.write(" “IN0000002”,“MEIJI”,“113.40”,“150” \n")
            test_file.write(" “IN0000002”,“PUCCHO”,“73.13”,“150” \n")
            test_file.write(" “IN0000003”,“POCKY”,“16.64”,“400” \n")
            test_file.write(" “IN0000003”,“PUCCHO”,“97.50”,“200” \n")
            test_file.write(" “IN0000005”,“PUCCHO”,“97.50”,“200” \n")
          

    def tearDown(self):
        # Clean up: Delete the temporary test file
        os.remove(self.test_file_path)

    def test_read_file_setup_teardown(self):
        # Create an instance of CSVDataFile and call read_file
        csv_file = CSVDataFile(self.test_file_path)
        csv_file.read_file()
        # Assert that the fields and data have been populated correctly
        expected_fields = ['CUSTOMER_CODE','FIRSTNAME','LASTNAME']
        expected_data = [['CUST0000010231','Maria','Alba'],['CUST0000010232','John','Dhoe'],['CUST0000010233','Carolina','Herera'],['CUST0000010234','Nick','Adersen']]

        csv_file = CSVDataFile(self.test_file_path2)
        csv_file.read_file()
        # Assert that the fields and data have been populated correctly
        expected_fields = ['CUSTOMER_CODE']
        expected_data = [['CUST0000010231'],['CUST0000010232'],['CUST0000010233']]

        csv_file = CSVDataFile(self.test_file_path3)
        csv_file.read_file()
        # Assert that the fields and data have been populated correctly
        expected_fields = ['CUSTOMER_CODE','INVOICE_CODE','AMOUNT','DATE']
        expected_data = [['CUST0000010231','IN0000001','105.50','01-Jan-2016'],['CUST0000010235','IN0000002','115.50','01-Jan-2016'],['CUST0000010233','IN0000003','35.50','01-Jan-2016'],['CUST0000010231','IN0000004','25.50','01-Jan-2016']]

        csv_file = CSVDataFile(self.test_file_path4)
        csv_file.read_file()
        # Assert that the fields and data have been populated correctly
        expected_fields = ['INVOICE_CODE','ITEM_CODE','AMOUNT','QUANTITY']
        expected_data = [['IN0000001','MEIJI','75.60','100'],['IN0000001','POCKY','10.40','250'],['IN0000001','PUCCHO','19.50','40'],['IN0000002','MEIJI','113.40','150'],['IN0000002','PUCCHO','73.13','150'],['IN0000003','POCKY','16.64','400'],['IN0000003','PUCCHO','97.50','200'],['IN0000005','PUCCHO','97.50','200']]

        self.assertEqual(csv_file.fields, expected_fields)
        self.assertEqual(csv_file.data, expected_data)
    
    def test_filter_data_based_on_customercode(self):
        # Create instances of CSVDataFile for the test files
        customer = CSVDataFile(self.test_file_path)
        customer_sample = CSVDataFile(self.test_file_path2)
        invoice = CSVDataFile(self.test_file_path3)
        invoice_item = CSVDataFile(self.test_file_path4)

        # Add test data to the files
        customer.fields=['CUSTOMER_CODE','FIRSTNAME','LASTNAME']
        customer.data = [['CUST0000010231', 'Maria', 'Alba'],
                         ['CUST0000010232', 'John', 'Dhoe'],
                         ['CUST0000010233', 'Carolina', 'Herera'],
                         ['CUST0000010234', 'Nick', 'Adersen']]
        
        customer_sample.data = [['CUST0000010231'],
                                ['CUST0000010232'],
                                ['CUST0000010233']]
        invoice.fields=['CUSTOMER_CODE','INVOICE_CODE','AMOUNT','DATE']
        invoice.data = [['CUST0000010231', 'IN0000001', '105.50', '01-Jan-2016'],
                        ['CUST0000010235', 'IN0000002', '115.50', '01-Jan-2016'],
                        ['CUST0000010233', 'IN0000003', '35.50', '01-Jan-2016'],
                        ['CUST0000010231', 'IN0000004', '25.50', '01-Jan-2016']]
        invoice_item.field=['INVOICE_CODE','ITEM_CODE','AMOUNT','QUANTITY']
        invoice_item.data = [['IN0000001', 'MEIJI', '75.60', '100'],
                             ['IN0000001', 'POCKY', '10.40', '250'],
                             ['IN0000001', 'PUCCHO', '19.50', '40'],
                             ['IN0000002', 'MEIJI', '113.40', '150'],
                             ['IN0000002', 'PUCCHO', '73.13', '150'],
                             ['IN0000003', 'POCKY', '16.64', '400'],
                             ['IN0000003', 'PUCCHO', '97.50', '200'],
                             ['IN0000005', 'PUCCHO', '97.50', '200']]
        
        # Set up the output folder and prefix
        prefix = "TEST_SMALL"
        output_folder = "test/test_files"

        # Call the function to filter data based on customer codes
        files_with_customer_code = [customer, invoice]
        desired_customers_code = ['CUST0000010231', 'CUST0000010232', 'CUST0000010233']
        filter_data_based_on_customercode(files_with_customer_code, desired_customers_code, prefix, output_folder)

        # Check if the filtered files are created
        filtered_customer_path = os.path.join(output_folder, f"{prefix}{os.path.basename(self.test_file_path)}")
        filtered_invoice_path = os.path.join(output_folder, f"{prefix}{os.path.basename(self.test_file_path3)}")

        self.assertTrue(os.path.exists(filtered_customer_path))
        self.assertTrue(os.path.exists(filtered_invoice_path))
       
        filtered_customer = CSVDataFile(filtered_customer_path)
        filtered_invoice = CSVDataFile(filtered_invoice_path)

        # Read the filtered files
        filtered_customer.read_file()
        filtered_invoice.read_file()
       

        # Assert that the fields and data in the filtered customer file are correct
        expected_filtered_customer_fields = ['CUSTOMER_CODE', 'FIRSTNAME', 'LASTNAME']
        expected_filtered_customer_data = [['CUST0000010231', 'Maria', 'Alba'],
                                        ['CUST0000010232', 'John', 'Dhoe'],
                                        ['CUST0000010233', 'Carolina', 'Herera']]

        self.assertEqual(filtered_customer.fields, expected_filtered_customer_fields)
        self.assertEqual(filtered_customer.data, expected_filtered_customer_data)

        # Assert that the fields and data in the filtered invoice file are correct
        expected_filtered_invoice_fields = ['CUSTOMER_CODE', 'INVOICE_CODE', 'AMOUNT', 'DATE']
        expected_filtered_invoice_data = [['CUST0000010231', 'IN0000001', '105.50', '01-Jan-2016'],
                                         ['CUST0000010233', 'IN0000003', '35.50', '01-Jan-2016'],['CUST0000010231', 'IN0000004', '25.50', '01-Jan-2016']]

        self.assertEqual(filtered_invoice.fields, expected_filtered_invoice_fields)
        self.assertEqual(filtered_invoice.data, expected_filtered_invoice_data)

        

      #Add different scenarios as needed
     