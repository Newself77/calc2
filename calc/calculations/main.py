"""Runs the program"""
from os import path
import shutil
from glob import glob
from .addition import Addition
from .subtraction import Subtraction
from .multiplication import Multiplication
from .division import Division


def main(input_folder, output_folder):
    # Your code here: import each of the CSV files
    """
    Each of these variables holds a pandas DataFrame object

    add_csv = pd.read_csv("add_1000.csv")
    sub_csv = pd.read_csv("subtraction_1000.csv")
    mlt_csv = pd.read_csv("multiplication_1000.csv")
    div_csv = pd.read_csv("division_1000.csv")
    """

    # creates 4 dataframes
    # add_csv = pd.read_csv("add_1000.csv")
    # sub_csv = pd.read_csv("subtraction_1000.csv")
    # mlt_csv = pd.read_csv("multiplication_1000.csv")
    # div_csv = pd.read_csv("division_1000.csv")

    # Your code here: handle the CSV files
    input_folder = path.abspath(path.normpath(input_folder))
    output_folder = path.abspath(path.normpath(output_folder))
    for filepath in (input_folder, output_folder):
        if not path.isdir(filepath):
            raise OSError(f"{input_folder!r} is not a valid folder")

    # running our calcs on the dataframes
    file_list = []
    results_list = []
    file_list.append(glob(path.join(input_folder, "a*.csv"))[0])
    add_calculations = Addition(file_list[-1])
    results_list.append(add_calculations.add())
    file_list.append(glob(path.join(input_folder, "s*.csv"))[0])
    sub_calculations = Subtraction(file_list[-1])
    results_list.append(sub_calculations.subtract())
    file_list.append(glob(path.join(input_folder, "m*.csv"))[0])
    multi_calculations = Multiplication(file_list[-1])
    results_list.append(multi_calculations.multiply())
    file_list.append(glob(path.join(input_folder, "d*.csv"))[0])
    div_calculations = Division(file_list[-1])
    file_list.append(div_calculations.divide())
    for file in file_list:
        destination = path.join(output_folder, path.basename(file))
        shutil.move(file, destination)
    return results_list


if __name__ == '__main__':
    input_dir = path.join(__file__, "../../../datamanager/csv_test_excel")
    output_dir = path.join(__file__, "../../../output_dir")
    main(input_dir, output_dir)
