# Feb 8th, 2019
# Zixin Zhang
# This script is the function in Python to return a user an .md files with all information
# of the dependencis and functions 


import pandas as pd
import numpy as np


def lib_write(input_path, output_path):

    """
    This function takes an input Python script and return a .md file that is a dataframe and with
    information of the dependencis used in the script.

    Parameters
    ---------
    input_path(string): the path to the input .py script
    output_path(string): the path to store the ouput .md file

    """
    df <- lib_count()

    df.to_csv(output_path)
