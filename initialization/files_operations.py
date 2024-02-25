import os

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

