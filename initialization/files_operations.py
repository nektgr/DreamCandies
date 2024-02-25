import os
from entities.Abstract_file import CSVDataFile
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO)
def list_files_in_folder(folder_path,exclude_file):
    """
    List files in the specified folder.

    Parameters:
    - folder_path (str): Path to the folder.

    Returns:
    - list: List of files in the folder.
    """
    try:
        # Get the list of files in the specified folder
        files = os.listdir(folder_path)
        
        # Filter out subdirectories, if any
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file)) and file != exclude_file]
        
        return files
    except FileNotFoundError as e:
        logging.error(f"Error: {str(e)}")
        return []
    
def list_files_with_customer_code(files_list,input_folder):
        """
        Extracts files with 'CUSTOMER_CODE' field from the given list of files.

        Parameters:
        - files_list (list): List of file names.
        - input_folder (str): Path to the input folder.

        Returns:
        - files_with_customer_code (list): List of CSVDataFile objects with 'CUSTOMER_CODE' field.
        - files_without_customer_code (list): List of CSVDataFile objects without 'CUSTOMER_CODE' field.
        - desired_customers_code (list): List of desired customers' data from 'CUSTOMER_SAMPLE.CSV'.
        """
        files_with_customer_code = []
        files_without_customer_code = []
        desired_customers=[]
        desired_customers_code=[]
        for file_name in files_list:
            file_path = os.path.join(input_folder, file_name)

            try:
                csv_file = CSVDataFile(file_path)
                csv_file.read_file()
            

                if file_name== 'CUSTOMER_SAMPLE.CSV': 
                    desired_customers.extend(csv_file.data)
                    

                if 'CUSTOMER_CODE' in csv_file.fields:
                    files_with_customer_code.append(csv_file)
                else:
                    files_without_customer_code.append(csv_file)

            except Exception as e:
                logging.error(f"Error processing file '{file_path}': {str(e)}")
        #Modified the desired customer in order to get the codes in a single flattened list
        for x in desired_customers:
            for element in x:
                desired_customers_code.append(element)
        
        return files_with_customer_code, files_without_customer_code,desired_customers_code

def filter_data_based_on_keyvalue(unmatched_file_path, matched_file_path, keyvalue, output_folder,prefix):
        """
        Filter data in unmatched_file based on matching keyvalue in matched_file.

        Parameters:
        - unmatched_file_path (str): Path to the unmatched datafile.
        - matched_file_path (str): Path to the file to be matched with.
        - keyvalue (str): Keyvalue to match on.
        - output_folder (str): Folder to save filtered data.
        - prefix (str): Prefix for the output file name.
        """
        # Read data from the unmatched datafile
        unmatched_file = CSVDataFile(unmatched_file_path)
        unmatched_file.read_file()

        # Read data from the file to be matched with
        matched_file = CSVDataFile(matched_file_path)
        matched_file.read_file()

        # Check if the keyvalue exists in both files
        if keyvalue in unmatched_file.fields and keyvalue in matched_file.fields:
            # Find the index of the keyvalue in both files
            unmatched_index = unmatched_file.fields.index(keyvalue)
            matched_index = matched_file.fields.index(keyvalue)

            # Filter data based on the matching condition
            filtered_data = [row for row in unmatched_file.data if row[unmatched_index] in [entry[matched_index] for entry in matched_file.data]]

            # Save filtered data to the output folder
            output_file_name = f"{prefix}{os.path.basename(unmatched_file_path)}"
            output_file_path = os.path.join(output_folder, output_file_name)
            try:
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    # Write header with double quotes
                    output_file.write('“' + '”,“'.join(unmatched_file.fields) + '”\n')

                    # Write filtered data with douvle quotes
                    for row in filtered_data:
                        output_file.write(','.join(['“' + value + '”' for value in row]) + '\n')

                logging.info(f"Filtered data saved to '{output_file_path}'.")
            except Exception as e:
                logging.error(f"Error writing to file '{output_file_path}': {str(e)}")
        else:
            logging.info(f"Keyvalue '{keyvalue}' not found in both files.{unmatched_file_path} {matched_file_path}Unable to apply matching condition.")

def filter_data_based_on_customercode(files_with_customer_code,flattened_desired_customers,prefix,output_folder):
        """
        Filter data in files_with_customer_code based on 'CUSTOMER_CODE' matching desired_list.

        Parameters:
        - files_with_customer_code (list): List of CSVDataFile instances.
        - flattened_desired_customers (list): List of desired customer codes.
        - prefix (str): Prefix for the output file name.
        - output_folder (str): Folder to save filtered data.
        """
        for file_with_customer_code in files_with_customer_code:
            #Filter data based on 'CUSTOMER_CODE' matching desired_list
            filtered_data = [row for row in file_with_customer_code.data if row[0] in flattened_desired_customers]
            # Save filtered data to the output folder with double quotes
            output_file_name = prefix + os.path.basename(file_with_customer_code.file_path)
            output_file_path = os.path.join(output_folder, output_file_name)
            try:
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    # Write header with double quotes
                    output_file.write('“' + '”,“'.join(file_with_customer_code.fields) + '”\n')

                    # Write filtered data with double quotes
                    for row in filtered_data:
                        output_file.write(','.join('“' + value + '”' for value in row) + '\n')

                logging.info(f"Filtered data saved to '{output_file_path}'.")
            except Exception as e:
                logging.error(f"Error writing to file '{output_file_path}': {str(e)}")
 
    