"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 26, 2022
Description: Writes JSON data to formatted CSV file
"""

import json

# pylint: disable = invalid-name
# pylint: disable = too-few-public-methods

class SatData:
    """Converts JSON data to CSV"""
    def __init__(self):
        self._data = "sat.json"
        with open(self._data, "r", encoding = "UTF-8") as data:
            self._data_dict = json.load(data)

    def save_as_csv(self, dbn):
        """Converts, saves dictionary from JSON object as CSV"""
        dbn.sort()
        new_dict = {}

        for (key, val) in self._data_dict.items():
            if isinstance(val, list):
                for line in val:
                    num = line[8]
                    if "," in line[9]:
                        line[9] = '"' + line[9] + '"'
                    if num in dbn:
                        new_dict.setdefault(num, line[9:])

        with open("output.csv", "w", encoding = "UTF-8") as fin:
            fin.write("DBN,School Name,Number of Test Takers,"
                      "Critical Reading Mean,Mathematics Mean,Writing Mean")
            fin.write("\n")

            for (key, val) in new_dict.items():
                while None in val:
                    val.remove(val[-1])
                    val.insert(-1, "")
                fin.write(key + ",")
                for item in val[0:4]:
                    fin.write(item + ",")
                fin.write(val[4])
                fin.write("\n")

sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418", "01M509", "01M539"]
sd.save_as_csv(dbns)
