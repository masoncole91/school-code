import unittest
from Library import LibraryItem, Book, Album, Movie, Patron, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("345", "Phantom Tollbooth", "Juster")
        self.album1 = Album("456", "...And His Orchestra", "The Fastbacks")
        self.movie1 = Movie("567", "Laputa", "Miyazaki")

        self.patron1 = Patron("abc", "Felicity")
        self.patron2 = Patron("bcd", "Waldo")

        self.lib = Library()
        self.lib.add_library_item(self.book1)
        self.lib.add_library_item(self.album1)
        self.lib.add_library_item(self.movie1)

        self.lib.add_patron(self.patron1)
        self.lib.add_patron(self.patron2)

        self.holdings = self.lib.get_holdings()
        self.members = self.lib.get_members()

    def test_inherit(self):
        """Tests if items inherit from parent class"""
        self.assertIsInstance(self.book1, LibraryItem)
        self.assertIsInstance(self.album1, LibraryItem)
        self.assertIsInstance(self.movie1, LibraryItem)

    def test_creator(self):
        """Tests if correct creator attribute"""
        author = self.book1.get_author()
        artist = self.album1.get_artist()
        director = self.movie1.get_director()

        self.assertIs(author, "Juster")
        self.assertIs(artist, "The Fastbacks")
        self.assertIs(director, "Miyazaki")

    def test_stored(self):
        """Tests if library holdings stores LibraryItem objects,
        Members stores Patron objects"""
        for item in self.holdings:
            self.assertIsInstance(item, LibraryItem)
        for person in self.members:
            self.assertIsInstance(person, Patron)

    def test_lookup(self):
        """Tests lookup for item, patron"""
        members = self.lib.get_members()
        holdings = self.lib.get_holdings()

        self.lib.add_patron(self.patron1)
        self.lib.add_library_item(self.book1)

        patron_is = self.lib.lookup_patron_from_id("abc")
        patron_none = self.lib.lookup_patron_from_id("xyz")

        item_is = self.lib.lookup_library_item_from_id("345")
        item_none = self.lib.lookup_library_item_from_id("000")

        self.assertIsNotNone(patron_is)
        self.assertIn(patron_is, members)
        self.assertIsNone(patron_none)
        self.assertIsNotNone(item_is)
        self.assertIn(item_is, holdings)
        self.assertIsNone(item_none)

    def test_same(self):
        """Tests if two items, patrons are unique"""
        book2 = Book("543", "Phantom Tollbooth", "Juster")
        patron3 = Patron("xyz", "Felicity")

        self.lib.add_library_item(book2)
        self.lib.add_patron(patron3)

        book1_title = self.book1.get_title()
        book2_title = book2.get_title()
        book1_obj = self.lib.lookup_library_item_from_id("345")
        book2_obj = self.lib.lookup_library_item_from_id("543")

        patron1_name = self.patron1.get_patron_name()
        patron3_name = patron3.get_patron_name()
        patron1_obj = self.lib.lookup_patron_from_id("abc")
        patron3_obj = self.lib.lookup_patron_from_id("xyz")

        self.assertIs(book1_title, book2_title)
        self.assertIsNot(book1_obj, book2_obj)
        self.assertIs(patron1_name, patron3_name)
        self.assertIsNot(patron1_obj, patron3_obj)

    def test_check_out(self):
        """Registered patron checks out available item,
        LibraryItem, Patron updated
        Increment date but no fine"""
        attempt = self.lib.check_out_library_item("abc", "345")

        felicity = self.book1.get_checked_out_by()
        felicity = felicity.get_patron_name()
        date = self.book1.get_date_checked_out()
        status = self.book1.get_location()
        felicity_log = self.patron1.get_checked_out_items()

        self.assertEqual(attempt, "check out successful")
        self.assertEqual(felicity, "Felicity")
        self.assertIsNotNone(date)
        self.assertEqual(status, "CHECKED_OUT")
        self.assertIsNotNone(felicity_log)

        for title in felicity_log:
            self.assertIs(title, self.book1)

    def test_faulty_check_out(self):
        """Unregistered patron checks out,
        Or patron checks out unregistered item"""
        attempt1 = self.lib.check_out_library_item("xyz", "345")
        attempt2 = self.lib.check_out_library_item("abc", "000")

        self.assertEqual(attempt1, "patron not found")
        self.assertEqual(attempt2, "item not found")

    def test_check_out_2(self):
        """Patrons checks out checked-out item"""
        self.lib.check_out_library_item("abc", "345")
        attempt = self.lib.check_out_library_item("bcd", "345")

        self.assertEqual(attempt, "item already checked out")

    def test_check_out_held(self):
        """Patron checks out item held by other patron"""
        self.lib.request_library_item("abc", "345")
        attempt = self.lib.check_out_library_item("bcd", "345")

        self.assertEqual(attempt, "item on hold by other patron")

    def test_check_out_request(self):
        """Patron checks out item they previously held"""
        self.lib.request_library_item("abc", "345")
        check_out = self.lib.check_out_library_item("abc", "345")
        requested_by = self.book1.get_requested_by()

        self.assertEqual(check_out, "check out successful")
        self.assertIsNone(requested_by)

    def test_return(self):
        """Patron returns item to shelf,
        Their checked_out_items is updated,
        Item's checked_out_by updated"""
        checked_out = self.patron1.get_checked_out_items()
        checked_out_by = self.book1.get_checked_out_by()

        self.lib.check_out_library_item("abc", "345")

        result = self.lib.return_library_item("345")

        status = self.book1.get_location()

        self.assertEqual(checked_out, [])
        self.assertEqual(status, "ON_SHELF")
        self.assertIsNone(checked_out_by, None)
        self.assertEqual(result, "return successful")

    def test_hold_return(self):
        """Patron returns item requested by other patron,
        Goes back on hold"""
        item = self.lib.lookup_library_item_from_id("345")
        self.lib.check_out_library_item("abc", "345")
        self.lib.request_library_item("bcd", "345")
        self.lib.return_library_item(item)

        request = self.book1.get_requested_by()
        status = self.book1.get_location()

        self.assertIsNotNone(request)
        self.assertEqual(status, "ON_HOLD")

    def test_none_return(self):
        """Patron returns item not in holdings"""
        attempt = self.lib.return_library_item("000")

        self.assertEqual(attempt, "item not found")

    def test_shelf_return(self):
        """Patron returns item not checked out"""
        attempt = self.lib.return_library_item("345")

        self.assertEqual(attempt, "item already in library")

    def test_faulty_request(self):
        """Tests attempt with unregistered patron,
        unregistered item"""
        attempt1 = self.lib.request_library_item("xyz", "345")
        attempt2 = self.lib.request_library_item("abc", "000")

        self.assertEqual(attempt1, "patron not found")
        self.assertEqual(attempt2, "item not found")

    def test_hold(self):
        """Patron holds item,
        Another tries to hold same item"""
        hold = self.lib.request_library_item("abc", "345")
        record = self.book1.get_requested_by()
        record = Patron.get_patron_name(record)
        location = self.book1.get_location()
        attempt = self.lib.request_library_item("bcd", "345")

        self.assertEqual(hold, "request successful")
        self.assertEqual(record, "Felicity")
        self.assertEqual(location, "ON_HOLD")
        self.assertEqual(attempt, "item already on hold")

    def test_faulty_pay(self):
        """Unregistered patron attempts to pay fine"""
        attempt = self.lib.pay_fine("000", 5)

        self.assertEqual(attempt, "patron not found")

    def test_pass_time(self):
        """Date increments after check-out"""
        self.lib.check_out_library_item("bcd", "567")

        for _ in range(5):
            self.lib.increment_current_date()

        date = self.lib.get_current_date()

        self.assertEqual(date, 5)

    def test_fine_inc(self):
        """Patron checks out book, album, movie,
        returns in 22 days"""
        self.lib.check_out_library_item("bcd", "345")
        self.lib.check_out_library_item("bcd", "456")
        self.lib.check_out_library_item("bcd", "567")

        for _ in range(22):
            self.lib.increment_current_date()

        fine = self.patron2.get_fine_amount()
        book_fine = (22 - 21) * 0.10
        album_fine = (22 - 14) * 0.10
        movie_fine = (22 - 7) * 0.10
        test_fine = book_fine + album_fine + movie_fine

        self.assertAlmostEqual(fine, test_fine)

    def test_pay_fine(self):
        """Patron from above pays fine"""
        self.lib.check_out_library_item("bcd", "345")
        self.lib.check_out_library_item("bcd", "456")
        self.lib.check_out_library_item("bcd", "567")

        for _ in range(22):
            self.lib.increment_current_date()

        result = self.lib.pay_fine("bcd", 2.4)

        fine = self.patron2.get_fine_amount()

        self.assertAlmostEqual(fine, 0)
        self.assertEqual(result, "payment successful")



if __name__ == "__main__":
    unittest.main()

# Checks out book, returns in 50 days, check date_checked_out, current date, fine owed
# six possible locations:
## ON_SHELF - CHECKED_OUT
## ON_SHELF - ON_HOLD
## ON_HOLD - CHECKED_OUT
## ON_HOLD - ON_SHELF
## CHECKED_OUT - ON_SHELF
## CHECKED_OUT - ON_HOLD
