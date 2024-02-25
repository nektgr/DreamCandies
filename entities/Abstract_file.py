from abc import ABC, abstractmethod

class AbstractDataFile(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.fields = []
        self.data = []

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def display_info(self):
        pass
 

class CSVDataFile(AbstractDataFile):

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
        # Assuming the first line contains the heading
            heading = file.readline().strip().split(',')
            self.fields = [field.strip('“”') for field in heading]  # Strip double quotes

        # Read the rest of the lines as data
            for line in file:
                data_row = line.strip().split(',')
                self.data.append([value.strip('“”') for value in data_row])  # Strip double quotes

    def display_info(self):
        print(f"File: {self.file_path}")
        print("Fields:", self.fields)
        print("Data:")
        for row in self.data:
            print(row)

    