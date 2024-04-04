from file import File
from file_controller import FileController

controller = FileController()

file = File(r"Files\students.csv")
controller.convert_csv_to_json(file)