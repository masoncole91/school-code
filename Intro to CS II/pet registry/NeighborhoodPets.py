"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 26, 2022
Description: Initializes JSON file to organize pet info
"""

import json

# pylint: disable = invalid-name

class NeighborhoodPets:
    """Stores methods for adding, deleting pet info,
    and saving or loading JSON files"""
    def __init__(self):
        self._pets = None
        self._pet_dict = {}

    def add_pet(self, name, species, owner):
        """Adds pet to memory,
        raises error if duplicate"""
        for key in self._pet_dict:
            if name == key:
                raise DuplicateNameError
        self._pet_dict.setdefault(name, [species, owner])

    def delete_pet(self, name):
        """Deletes pet from memory"""
        new_pet_dict = {}
        for (key, val) in self._pet_dict.items():
            if name != key:
                new_pet_dict.setdefault(key, val)
        self._pet_dict = new_pet_dict

    def get_all_species(self):
        """Returns all species in pet data"""
        species = []
        for (_, val) in self._pet_dict.items():
            species.append(val[0])
        return species

    def get_owner(self, name):
        """Accesses dictionary value pet owner"""
        owner = None
        for (key, val) in self._pet_dict.items():
            if name == key:
                owner = val[-1]
        return owner

    def read_json(self, fin):
        """Loads JSON file, replacing current pets in memory"""
        with open(fin, "r", encoding = "UTF-8") as infile:
            self._pets = json.load(infile)

    def save_as_json(self, fin):
        """Writes pet dictionary to JSON file"""
        with open(fin, "w", encoding = "UTF-8") as outfile:
            pets_json = json.dumps(self._pet_dict)
            outfile.write(pets_json)

class DuplicateNameError(Exception):
    """Raises error if two pets with same name found"""
