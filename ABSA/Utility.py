"""Instantiate model and create tools for running basic ASBA from input

Created by Griffin Gooch-Breault 4/7/2025
"""

import csv


def read_csv_as_list(path):
    """Function to return CSVs as lists."""
    file = open(path, encoding="utf8")
    csv_file = csv.reader(file)

    # this takes 0th element, our CSVs only have one column
    lines = [i[0] for i in csv_file]
    return lines
