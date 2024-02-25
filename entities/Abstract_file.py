"""
Module containing an abstract base class for representing a generic data file.
"""
from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO)
class AbstractDataFile(ABC):
    """
    Abstract base class representing a generic data file. Subclasses must implement
    the read_file and display_info methods.
    """
    def __init__(self, file_path):
        """
        Constructor for AbstractDataFile.

        Parameters:
        - file_path (str): The path to the data file.
        """
        self.file_path = file_path
        self.fields = []
        self.data = []

    @abstractmethod
    def read_file(self):
        """
        Abstract method to be implemented by subclasses for reading data from the file.
        """
        pass

    @abstractmethod
    def display_info(self):
        """
        Abstract method to be implemented by subclasses for displaying information about the file.
        """
        pass
 

class CSVDataFile(AbstractDataFile):
    """
    Concrete implementation of AbstractDataFile for CSV (Comma-Separated Values) files.
    """
    def read_file(self):
        """
        Implementation of read_file for CSVDataFile. Reads data from the CSV file and populates
        the fields and data attributes.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
            # Assuming the first line contains the heading
                heading = file.readline().strip().split(',')
                self.fields = [field.strip('“”') for field in heading]  # Strip double quotes

            # Read the rest of the lines as data
                for line in file:
                    data_row = line.strip().split(',')
                    self.data.append([value.strip('“”') for value in data_row])  # Strip double quotes
        except Exception as e:
            logging.error(f"Error reading file '{self.file_path}': {str(e)}")

    def display_info(self):
        """
        Implementation of display_info for CSVDataFile. Displays information about the CSV file,
        including file path, fields, and data rows.
        """
        print(f"File: {self.file_path}")
        print("Fields:", self.fields)
        print("Data:")
        for row in self.data:
            print(row)

    