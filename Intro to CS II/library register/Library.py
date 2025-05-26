"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 12, 2022
Description: Simulates a library system with logged check-outs, on-hold items, and accrued fines
"""

# pylint: disable = invalid-name

class LibraryItem:
    """Parent class for Book, Album, Movie;
    stores library item data for patrons"""
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None
        self._location = "ON_SHELF"

    def set_checked_out_by(self, patron):
        """Links checked-out item to Patron object"""
        self._checked_out_by = patron
        return self._checked_out_by

    def set_requested_by(self, patron):
        """Links on-hold item to Patron object"""
        self._requested_by = patron
        return self._requested_by

    def set_date_checked_out(self, date):
        """Links check-out to current date for fine accruement"""
        self._date_checked_out = date
        return self._date_checked_out

    def set_location(self, new_status):
        """Changes string status of item"""
        self._location = new_status
        return self._location

    def get_library_item_id(self):
        """Accesses item ID string, not its object"""
        return self._library_item_id

    def get_title(self):
        """Accesses string title of item"""
        return self._title

    def get_checked_out_by(self):
        """Accesses patron who has item checked out"""
        return self._checked_out_by

    def get_requested_by(self):
        """Accesses Patron object for on-hold item"""
        return self._requested_by

    def get_date_checked_out(self):
        """Accesses integer day a patron checked out an item"""
        return self._date_checked_out

    def get_location(self):
        """Accesses if item available, on-hold, checked out"""
        return self._location

class Book(LibraryItem):
    """Child class for LibraryItem,
    stores book item-specific data: check-out length, author"""
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Accesses string book item-author"""
        return self._author

    def get_check_out_length(self):
        """Accesses how many days patrons can check-out book items"""
        return 21

class Album(LibraryItem):
    """Child class for LibraryItem,
    stores album item-specific data: check-out length, artist"""
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Accesses string album item-artist"""
        return self._artist

    def get_check_out_length(self):
        """Accesses how many days patrons can check-out album items"""
        return 14

class Movie(LibraryItem):
    """Child class for LibraryItem,
    stores album item-specific data: check-out length, director"""
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """Accesses string movie item-director"""
        return self._director

    def get_check_out_length(self):
        """Accesses how many days patrons can check-out movie items"""
        return 7

class Patron:
    """Stores library visitor data"""
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def add_library_item(self, item):
        """Used to add item upon patron check-out"""
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """Used to remove item up on patron check-in"""
        self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        """Changes patron's fine amount,
        can be negative or positive"""
        self._fine_amount += amount
        return self._fine_amount

    def get_patron_id(self):
        """Accesses string alphanumeric patron ID"""
        return self._patron_id

    def get_patron_name(self):
        """Accesses string patron name"""
        return self._name

    def get_checked_out_items(self):
        """Accesses array of LibraryItem objects
        for items currently checked out by patron"""
        return self._checked_out_items

    def get_fine_amount(self):
        """Accesses float fine patron owes in dollars"""
        return self._fine_amount

class Library:
    """Implements check-out, return, on-hold mechanics for library system"""
    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def check_out_library_item(self, patron_num, item_num):
        """Lets patron check-out item,
         Updates item, patron status"""
        media = LibraryItem
        patron = Patron

        item_obj = self.lookup_library_item_from_id(item_num)
        patron_obj = self.lookup_patron_from_id(patron_num)

        if patron_obj is None:
            return "patron not found"
        if item_obj is None:
            return "item not found"

        status = media.get_location(item_obj)

        if status == "CHECKED_OUT":
            return "item already checked out"
        if status == "ON_HOLD":
            request = media.get_requested_by(item_obj)
            if request != patron_obj:
                return "item on hold by other patron"

        media.set_checked_out_by(item_obj, patron_obj)
        media.set_date_checked_out(item_obj, self._current_date)
        media.set_location(item_obj, "CHECKED_OUT")
        media.set_requested_by(item_obj, None)
        patron.add_library_item(patron_obj, item_obj)

        return "check out successful"

    def return_library_item(self, item_num):
        """Lets patrons return items,
        updates item, patron status"""
        media = LibraryItem
        patron = Patron

        item_obj = self.lookup_library_item_from_id(item_num)

        if item_obj not in self._holdings:
            return "item not found"

        status = media.get_location(item_obj)

        if status != "CHECKED_OUT":
            return "item already in library"

        patron_obj = LibraryItem.get_checked_out_by(item_obj)
        patron.remove_library_item(patron_obj, item_obj)
        media.set_location(item_obj, "ON_SHELF")
        media.set_checked_out_by(item_obj, None)
        return "return successful"

    def request_library_item(self, patron_num, item_num):
        """Holds items for patrons,
        forbids multiple holds for same item"""
        media = LibraryItem

        item_obj = self.lookup_library_item_from_id(item_num)
        patron_obj = self.lookup_patron_from_id(patron_num)

        if patron_obj is None:
            return "patron not found"
        if item_obj is None:
            return "item not found"

        status = media.get_location(item_obj)
        request = media.get_requested_by(item_obj)

        if status == "ON_HOLD":
            if request is not patron_obj:
                return "item already on hold"
        media.set_location(item_obj, "ON_HOLD")
        media.set_requested_by(item_obj, patron_obj)
        return "request successful"

    def pay_fine(self, patron_num, amount):
        """Reduces fine if patron pays amount,
        updates Patron object"""
        patron = Patron
        amount = amount * -1
        patron_obj = self.lookup_patron_from_id(patron_num)

        if patron_obj is None:
            return "patron not found"

        patron.amend_fine(patron_obj, amount)
        return "payment successful"

    def increment_current_date(self):
        """Updates current date,
        Accrues fine of $0.10 daily for overdue patrons"""
        media = LibraryItem
        self._current_date += 1

        for item in self._holdings:
            patron_obj = media.get_checked_out_by(item)
            if patron_obj is not None:
                days = self._current_date - media.get_date_checked_out(item)
                if isinstance(item, Book) and days > Book.get_check_out_length(item):
                    patron_obj.amend_fine(0.10)
                if isinstance(item, Album) and days > Album.get_check_out_length(item):
                    patron_obj.amend_fine(0.10)
                if isinstance(item, Movie) and days > Movie.get_check_out_length(item):
                    patron_obj.amend_fine(0.10)

    def lookup_library_item_from_id(self, item_id):
        """Returns LibraryItem object by string ID,
         None if nonexistent"""
        for item in self._holdings:
            media = LibraryItem
            num = media.get_library_item_id(item)
            if item_id == num:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """Returns Patron object by string ID,
        None if nonexistent"""
        for person in self._members:
            patron = Patron
            member = patron.get_patron_id(person)
            if patron_id == member:
                return person
        return None

    def add_library_item(self, item_obj):
        """Registers media item as accessible to patrons"""
        self._holdings.append(item_obj)

    def add_patron(self, patron_obj):
        """Registers patron in library members list"""
        self._members.append(patron_obj)

    def get_holdings(self):
        """Accesses list of LibraryItem objects
        as library items offered"""
        return self._holdings

    def get_members(self):
        """Accesses list of Patron objects
        as registered library patrons"""
        return self._members

    def get_current_date(self):
        """Accesses integer as current date"""
        return self._current_date
