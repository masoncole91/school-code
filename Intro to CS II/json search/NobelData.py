"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 26, 2022
Description: Reads JSON file, returns sorted data in array
"""

import json

# pylint: disable = invalid-name
# pylint: disable = too-few-public-methods

class NobelData:
    """Initalizes JSON infile, searches and sorts data"""
    def __init__(self):
        with open("nobels.json", "r", encoding = "UTF-8") as infile:
            self._nobels_dict = json.load(infile)

    def search_nobel(self, year, category):
        """Accesses nested data,
        returns sorted array"""
        array = []
        for (_, val) in self._nobels_dict.items():
            for line in val:
                if line["year"] == year and line["category"] == category:
                    for winner in line["laureates"]:
                        array.append(winner["surname"])
        return sorted(array)
