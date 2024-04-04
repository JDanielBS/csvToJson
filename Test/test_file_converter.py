'''Module for the tests of the FileController class'''

import unittest
from Converter.file_controller import FileController
from Converter.file import File

class TestFiles(unittest.TestCase):
    '''Test class for the FileController class'''

    def test_route_found(self):
        '''Test for the convert_csv_to_json method when the file exists'''

        controller = FileController()
        file = File(r".\Files\students.csv")
        self.assertIsNotNone(controller.convert_csv_to_json(file))
    def test_route_not_found(self):
        '''Test for the convert_csv_to_json method when the file does not exist'''

        controller = FileController()
        file = File(r".\Files\xyz.csv")
        with self.assertRaises(FileNotFoundError):
            controller.convert_csv_to_json(file)
    def test_extension(self):
        '''Test for the convert_csv_to_json method when the file has the wrong extension'''

        controller = FileController()
        file = File(r".\Files\students.txt")
        self.assertIsNone(controller.convert_csv_to_json(file))
    def test_wrong_number_of_columns(self):
        '''Test for the convert_csv_to_json method when a row has the wrong number of columns'''

        controller = FileController()
        file = File(r".\Files\students_wrong_columns.csv")
        self.assertIsNotNone(controller.convert_csv_to_json(file))
