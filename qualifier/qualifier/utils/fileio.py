# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


output_path = Path("qualifying_loans.csv")

def save_csv(output_path):
    """Saves CSV file in output path
    
    Args:
        qualiying_loans (list)

    Returns:
        A CSV file with rows of data from qualiying_loans
    
    """

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        for loan in qualifying_loans:
            csvwriter.writerow(loan.values())



