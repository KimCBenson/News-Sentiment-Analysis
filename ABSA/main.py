"""Main project file responsible for handling mass analysis of CSVs

Created by Griffin Gooch-Breault 4/7/2025
"""

import ABSA
import Utility

ASPECT_FILE_PATH = ""
TEXTS_FILE_PATH = ""


if __name__ == "__main__":
    aspects = Utility.read_csv_as_list(ASPECT_FILE_PATH)
    texts = Utility.read_csv_as_list(TEXTS_FILE_PATH)

    out = ABSA.list_absa(aspects, texts)

    print(out)
