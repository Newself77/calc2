# show Current working directory
import pandas as pd

import os

os.getcwd()

with open("add_1000.csv", 'r') as infile:
    reader = pd.read_csv(infile, delimiter=",")
    header = next(reader)
    for row in reader:
        add_value_1 = row[0]
        add_value_2 = row[1]
        add_result = row[2]
        print(add_value_1, add_value_2, add_result)
