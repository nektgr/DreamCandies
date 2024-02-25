import os
from initialization.files_operations import filter_data_based_on_keyvalue, list_files_in_folder,copy_files_to_output
from entities.Abstract_file import CSVDataFile

def list_files_with_customer_code(files_list,input_folder):
        files_with_customer_code = []
        files_without_customer_code = []
        desired_customers_code=[]
        for file_name in files_list:
            file_path = os.path.join(input_folder, file_name)

            csv_file = CSVDataFile(file_path)
            csv_file.read_file()
            csv_file.display_info()

            if file_name== 'CUSTOMER_SAMPLE.CSV': 
                desired_customers_code.extend(csv_file.data)

            if 'CUSTOMER_CODE' in csv_file.fields:
                files_with_customer_code.append(csv_file)
            else:
                files_without_customer_code.append(csv_file)

        return files_with_customer_code, files_without_customer_code,desired_customers_code

def main():
    folder_path = "input_files"  # You can change this to your desired folder path
    exclude_file = "CUSTOMER_SAMPLE.CSV"  # Specify the file to be excluded
    input_folder = "input_files"
    output_folder = "output_files"
    prefix = "SMALL_"

    # Get the list of files in the folder
    files_list = list_files_in_folder(folder_path)

    # Copy the files to the output folder (excluding specified file) with prefix 'SMALL_'
    #copy_files_to_output(files_list, exclude_file, input_folder, output_folder, prefix)
   

    files_with_customer_code, files_without_customer_code,desired_customers_code = list_files_with_customer_code(files_list,input_folder)
    
    #we managed to this point to separate the input files to those that they have customer_code (easy case scenario handling)
    flattened_desired_customers = []
    for x in desired_customers_code:
        for element in x:
            flattened_desired_customers.append(element)
    #print(flattened_desired_customers)

    #for x in files_with_customer_code:
    #    print(x.data)
    for file_with_customer_code in files_with_customer_code:
        print("Original Data:", file_with_customer_code.file_path)

    #    Filter data based on 'CUSTOMER_CODE' matching desired_list
        filtered_data = [row for row in file_with_customer_code.data if row[0] in flattened_desired_customers]

    # Save filtered data to the output folder with double quotes
        output_file_name = prefix + os.path.basename(file_with_customer_code.file_path)
        output_file_path = os.path.join(output_folder, output_file_name)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write header with double quotes
            output_file.write('“' + '”,“'.join(file_with_customer_code.fields) + '”\n')

            # Write filtered data with double quotes
            for row in filtered_data:
                output_file.write(','.join('“' + value + '”' for value in row) + '\n')

        print(f"Filtered data saved to '{output_file_path}'.")




        #based on the input from the user he will state ["unmatched datafile",'file to be matched with','keyvalue']
        
    match_conditions=[[f'{input_folder}/INVOICE_ITEM.csv',f'{output_folder}/{prefix}INVOICE.csv','INVOICE_CODE']]
    for condition in match_conditions:
        filter_data_based_on_keyvalue(condition[0], condition[1], condition[2], output_folder, prefix, file_with_customer_code)

if __name__ == "__main__":
    main()