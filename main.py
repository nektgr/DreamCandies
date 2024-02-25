from initialization.files_operations import list_files_in_folder,copy_files_to_output


def main():
    folder_path = "input_files"  # You can change this to your desired folder path
    exclude_file = "CUSTOMER_SAMPLE.CSV"  # Specify the file to be excluded
    input_folder = "input_files"
    output_folder = "output_files"
    prefix = "SMALL_"

    # Get the list of files in the folder
    files_list = list_files_in_folder(folder_path)

    # Copy the files to the output folder (excluding specified file) with prefix 'SMALL_'
    copy_files_to_output(files_list, exclude_file, input_folder, output_folder, prefix)

if __name__ == "__main__":
    main()