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


def remove_unrelated(texts, word):
    out = []

    # remove any headlines that do not have the keyword
    for t in texts:
        if word.lower() in t.lower():
            out.append(t)

    return out


def generate_aspect_csv():
    """This just automates creating a csv for the aspects"""

    filepath = ""
    data = [
        # This aspect list is currently incomplete
        # Note: it should also be cut down, it is currently not specific enough.
        # People
        {'Aspect': 'Jeff Bezos'},
        {'Aspect': 'Bezos'},
        {'Aspect': 'Joe Biden'},
        {'Aspect': 'Biden'},
        {'Aspect': 'Elon Musk'},
        {'Aspect': 'Musk'},
        {'Aspect': 'Vladimir Putin'},
        {'Aspect': 'Putin'},
        {'Aspect': 'Donald Trump'},
        {'Aspect': 'Trump'},
        {'Aspect': 'Volodymyr Zelenskyy'},
        {'Aspect': 'Volodymyr Zelensky'},
        {'Aspect': 'Zelensky'},

        # Places
        {'Aspect': 'Ukraine'},
        {'Aspect': 'Russia'},
        {'Aspect': 'China'},
        {'Aspect': 'Mexico'},
        {'Aspect': 'Canada'},
        {'Aspect': 'Israel'},
        {'Aspect': 'Palestine'},
        {'Aspect': 'US'},
        {'Aspect': 'USA'},
        {'Aspect': 'America'},
        {'Aspect': 'Gaza'},
        {'Aspect': 'Washington'},
        {'Aspect': 'Moscow'},
        {'Aspect': 'White House'},
        {'Aspect': 'Puerto Rico'},

        # Demographics
        {'Aspect': 'Hispanic'},
        {'Aspect': 'Latin'},
        {'Aspect': 'Latino'},
        {'Aspect': 'Latina'},
        {'Aspect': 'Native Hawaiian'},
        {'Aspect': 'Alaska Native'},
        {'Aspect': 'Native American'},
        {'Aspect': 'Navajo'},
        {'Aspect': 'Abenaki'},
        {'Aspect': 'Asian'},
        {'Aspect': 'White'},
        {'Aspect': 'Black'},
        {'Aspect': 'African American'},
        {'Aspect': 'Queer'},
        {'Aspect': 'Gay'},
        {'Aspect': 'Trans'},
        {'Aspect': 'Transgender'},
        {'Aspect': 'Disabled'},
        {'Aspect': 'Veteran'},
        {'Aspect': 'Homeless'},
        {'Aspect': 'Citizen'},
        {'Aspect': 'Undocumented'},
        {'Aspect': 'Immigrant'},
        {'Aspect': 'Migrant'},
        {'Aspect': 'Employed'},
        {'Aspect': 'Unemployed'},
        {'Aspect': 'Male'},
        {'Aspect': 'Female'},
        {'Aspect': 'Man'},
        {'Aspect': 'Woman'},

        # MSC
        {'Aspect': 'Police'},
        {'Aspect': 'LGBTQ+'}
    ]

    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ['Aspect']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
