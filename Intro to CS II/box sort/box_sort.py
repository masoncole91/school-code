"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 18, 2022
Description: Sorts list of Box objects from greatest to least volume
"""

class Box:
    """Stores Box objects for outside function box_sort()"""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """Computes volume of box"""
        return self._length * self._width * self._height

    def get_length(self):
        """Accesses private variable length"""
        return self._length

    def get_width(self):
        """Accesses private variable width"""
        return self._width

    def get_height(self):
        """Accesses private variable height"""
        return self._height

def box_sort(array):
    """Sorts list of Box objects from greatest to least volume by mutation"""
    box = Box
    for (index, obj) in enumerate(array):
        pos = index - 1
        while pos >= 0 and box.volume(array[pos]) < box.volume(obj):
            array[pos + 1] = array[pos]
            pos -= 1
        array[pos + 1] = obj
