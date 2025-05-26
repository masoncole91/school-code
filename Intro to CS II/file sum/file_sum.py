"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 26, 2022
Description: Sums list of numbers from plain text file, writes to sum.txt
"""

def file_sum(fin):
    """Opens text file, converts strings to floats,
     sums digits, writes to new file"""
    amount = 0

    with open(fin, "r", encoding = "UTF-8") as num:
        for line in num:
            line = line.strip()
            line = float(line)
            amount += line

    amount = str(amount)

    with open("sum.txt", "w", encoding = "UTF-8") as num:
        num.write(amount)
