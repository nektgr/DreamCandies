"""
Main script for executing the DreamCandies File Tool.

This script orchestrates the process of filtering and matching data files for the DreamCandies project.
"""
from initialization.files_operations import filter_data_based_on_customercode, filter_data_based_on_keyvalue, list_files_in_folder, list_files_with_customer_code

def main():
    """
    Main function to execute the DreamCandies File Tool.

    It performs the following steps:
    1. List files in the specified folder.
    2. Extract files with 'CUSTOMER_CODE' field.
    3. Filter data based on customer codes.
    4. Filter data that do not have customer codes based number 3 result.

    Note: Modify input_folder, exclude_file,output_folder and match_conditions as needed.
    """
    input_folder = "input_files" 
    output_folder = "output_files"
    prefix = "SMALL_"
    #Insert in match_conditions a list of [File to be Matched, File to match with, keyvalue] 
    match_conditions=[[f'{input_folder}/INVOICE_ITEM.csv',f'{output_folder}/{prefix}INVOICE.csv','INVOICE_CODE']]
    # Get the list of files in the folder
    files_list = list_files_in_folder(input_folder)
    #files_without_customer_code is not used for now but migth used in the future
    files_with_customer_code, files_without_customer_code,desired_customers_code = list_files_with_customer_code(files_list,input_folder)

    filter_data_based_on_customercode(files_with_customer_code,desired_customers_code,prefix,output_folder)
        
    
    for condition in match_conditions:
        filter_data_based_on_keyvalue(condition[0], condition[1], condition[2], output_folder, prefix)

if __name__ == "__main__":
    main()