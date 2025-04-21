"""Main project file responsible for handling mass analysis of CSVs

Created by Griffin Gooch-Breault 4/7/2025
"""

import ABSA
import Utility
import csv

ASPECT_FILE_PATH = \
    "C:\\Users\\cgb\\Desktop\\local_nsa_things\\submission5\\Generated Data\\Aspects\\Aspects.csv"
TEXTS_FILE_PATH = \
    "C:\\Users\\cgb\\Desktop\\local_nsa_things\\submission5\\dataset\\raw_news_titles\\nytarticles.csv"
OUTPUT_CSV_PATH = \
    "C:\\Users\\cgb\\Desktop\\local_nsa_things\\submission5\\Generated Data\\Analysis\\NYT\\NYT.csv"


if __name__ == "__main__":
    """Save analysis data in OUTPUT_CSV_PATH from all titles in TEXTS_FILE_PATH from ASPECT_FILE_PATH
    """
    aspects = Utility.read_csv_as_list(ASPECT_FILE_PATH)
    texts = Utility.read_csv_as_list(TEXTS_FILE_PATH)
    
    # remove header
    aspects.remove("Aspect")

    data = []

    for a in aspects:
        print(a)
        relevant_data = Utility.remove_unrelated(texts, a)
        print(relevant_data)

        # indicate missing data on data set
        if len(relevant_data) == 0:
            data.append( \
                {'Negative Aspect': 0.0,
                 'Neutral Aspect': 0.0,
                 'Positive Aspect': 0.0,
                 'Aspect': a,
                 'Data Pool Size': 0
                 })
            continue

        # Run analysis
        out = ABSA.avg_list_absa(a, relevant_data)

        # Format data
        data.append(\
            {'Negative Aspect': out[0],
             'Neutral Aspect': out[1],
             'Positive Aspect': out[2],
             'Aspect': a,
             'Data Pool Size': len(relevant_data)
             })

    # add data to csv
    with open(OUTPUT_CSV_PATH, 'w', newline='') as csvfile:
        fieldnames = ['Negative Aspect', 'Neutral Aspect', 'Positive Aspect', 'Aspect', 'Data Pool Size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
