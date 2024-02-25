import os
from initialization.files_operations import list_files_in_folder,copy_files_to_output
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
  

    for x in files_with_customer_code:
        filtered_data = [row for row in x.data if row[0] in flattened_desired_customers]

    #filtered_Data now contains only the desired files

if __name__ == "__main__":
    main()