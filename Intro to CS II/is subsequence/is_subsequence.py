"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov. 2, 2022
Description: Recursively determines string subsets
"""

def is_subsequence(str1, str2):
    """Runs function rec_is_subsequence,
     determines string subsets"""
    return rec_is_subsequence(str1, str2, 0)

def rec_is_subsequence(str1, str2, pos):
    """Sets two strings,
    determines if first string can result
    from characters of second string"""
    if str1 == "":
        return True
    if str2 == "":
        return False
    if str1 == str2:
        return True
    if len(str2) < len(str1):
        return False

    str1, str2 = str1.lower(), str2.lower()
    str1, str2 = sorted(str1), sorted(str2)
    str1, str2 = "".join(str1), "".join(str2)

    if str2[pos] not in str1:
        str2 = str2[pos + 1:] + str2[:pos]
        return rec_is_subsequence(str1, str2, pos)

    return rec_is_subsequence(str1, str2, pos + 1)
