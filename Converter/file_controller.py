'''Module that provides the FileController class'''

import csv
import json
import os
from Converter.file import File

class FileController:
    '''
    FileController class is responsible for manipulating files.

    ...

    Methods
    -------
    convert_csv_to_json(file: File)
        gets the content of a csv file and converts it to a json file
    get_name_with_path(path: str)
        gets the name of a file (without the extension) with its path
    '''

    def convert_csv_to_json(self, file) -> File:
        '''
        Converts a csv file to a json file, taking into account that the keys of the rows
        of the files to take into account are in this order: id, name, lastName

        Parameters
        ----------
        file: File
            the file to be converted to json
        '''

        if os.path.exists(file.get_path()):
            if not file.get_path().endswith(".csv"):
                print("The file has the wrong extension")
                return None
            data = []
            file_name = self.get_name_with_path(file.get_path())
            new_path = file.get_path().replace(f"{file_name}.csv", f"{file_name}.json")
            with open(file.get_path(), 'r', encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if len(row) != 3:
                        print("The row '" + str(row) + "' does not have the correct number of columns")
                        continue
                    data.append({"id": row[0], "name": row[1], "lastName": row[2]})
            with open(new_path, 'w', encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)

            print("The file has been converted to json")
            return File(new_path)
        else:
            print("The file does not exist")
            raise FileNotFoundError("The file does not exist")

    def get_name_with_path(self, path: str) -> str:
        '''
        Returns the name of a file (without the extension) with its path

        Parameters
        ----------
        path: str
            the path of the file in the file system
        '''

        return path.split('\\')[-1].split('.')[0]
