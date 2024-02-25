import os
from initialization.files_operations import filter_data_based_on_customercode, filter_data_based_on_keyvalue, list_files_in_folder, list_files_with_customer_code
from entities.Abstract_file import CSVDataFile

def main():
    folder_path = "input_files"  # You can change this to your desired folder path
    exclude_file = "CUSTOMER_SAMPLE.CSV"  # Specify the file to be excluded
    input_folder = "input_files" 
    output_folder = "output_files"
    prefix = "SMALL_"

    # Get the list of files in the folder
    files_list = list_files_in_folder(folder_path)
    files_with_customer_code, files_without_customer_code,desired_customers_code = list_files_with_customer_code(files_list,input_folder)
    
    flattened_desired_customers = []
    for x in desired_customers_code:
        for element in x:
            flattened_desired_customers.append(element)

    filter_data_based_on_customercode(files_with_customer_code,flattened_desired_customers,prefix,output_folder)
        
    match_conditions=[[f'{input_folder}/INVOICE_ITEM.csv',f'{output_folder}/{prefix}INVOICE.csv','INVOICE_CODE']]
    for condition in match_conditions:
        filter_data_based_on_keyvalue(condition[0], condition[1], condition[2], output_folder, prefix)

if __name__ == "__main__":
    main()