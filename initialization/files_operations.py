import os
from entities.Abstract_file import CSVDataFile

def list_files_in_folder(folder_path):
    try:
        # Get the list of files in the specified folder
        files = os.listdir(folder_path)
        
        # Filter out subdirectories, if any
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        
        return files
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
        return []

def copy_files_to_output(files_list, exclude_file, input_folder, output_folder, prefix):
    try:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Copy each file from the input folder to the output folder (excluding specified file)
        for file_name in files_list:
            if file_name != exclude_file:
                source_path = os.path.join(input_folder, file_name)
                destination_name = prefix + file_name
                destination_path = os.path.join(output_folder, destination_name)

                with open(source_path, 'rb') as source_file, open(destination_path, 'wb') as destination_file:
                    # Read content from source file and write it to destination file
                    destination_file.write(source_file.read())

        print(f"Files copied from '{input_folder}' to '{output_folder}' (excluding '{exclude_file}') with '{prefix}' prefix.")
    except Exception as e:
        print(f"Error copying files: {e}")

def filter_data_based_on_keyvalue(unmatched_file_path, matched_file_path, keyvalue, output_folder,prefix,file_with_customer_code):
        # Read data from the unmatched datafile
        unmatched_file = CSVDataFile(unmatched_file_path)
        unmatched_file.read_file()
        print(unmatched_file.fields)

        # Read data from the file to be matched with
        matched_file = CSVDataFile(matched_file_path)
        matched_file.read_file()
        print(matched_file.fields)

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

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                # Write header with double quotes
                output_file.write('“' + '”,“'.join(file_with_customer_code.fields) + '”\n')

                # Write filtered data with douvle quotes
                for row in filtered_data:
                    output_file.write(','.join(['“' + value + '”' for value in row]) + '\n')

            print(f"Filtered data saved to '{output_file_path}'.")
        else:
            print(f"Keyvalue '{keyvalue}' not found in both files. Unable to apply matching condition.")

 
    