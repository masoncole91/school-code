"""
Mason Blanford
Oct. 3, 2022
Unit tests LemonadeStand.py
"""

# pylint: disable = invalid-name

import unittest
from LemonadeStand import LemonadeStand, MenuItem     # pylint: disable = import-error

class TestLemonadeStand(unittest.TestCase):
    """Unit tests for LemonadeStand.py"""

    def setUp(self):
        self.stand = LemonadeStand("Leninist Lemons")
        self.item1 = MenuItem("Das Kapital Kool-Aid", 0.5, 2.0)
        self.item2 = MenuItem("class cake", 2.0, 3.5)
        self.item3 = MenuItem("Bolshevik bingsu", 5.0, 11.5)
        self.stand.add_menu_item(self.item1)
        self.stand.add_menu_item(self.item2)
        self.stand.add_menu_item(self.item3)

        day_one_log = {"Das Kapital Kool-Aid": 5.0,
                "class cake": 7.0}
        day_two_log = {"Bolshevik bingsu": 3.0,
                       "class cake": 3.0}
        day_three_log = {"Das Kapital Kool-Aid": 2.0,
                         "Bolshevik bingsu": 7.0}

        self.stand.enter_sales_for_today(day_one_log)
        self.stand.enter_sales_for_today(day_two_log)
        self.stand.enter_sales_for_today(day_three_log)

    def test_name(self):
        """Tests if the lemonade stand's name is set"""
        name = self.stand.get_name()
        self.assertIs(name, "Leninist Lemons")

    def test_menu_add(self):
        """Tests if the dictionary stores menu items"""
        name = MenuItem.get_name(self.item1)
        dvar = self.stand.get_menu()
        self.assertIn(name, dvar)

    def test_sales_add(self):
        """Tests if current day increments,
        if sales records are list types"""
        day = self.stand.get_current_day()
        lst = self.stand.get_sales_record()
        self.assertGreater(day, 1)
        self.assertIsInstance(lst, list)

    def test_sales(self):
        """Tests for correct amount sold of an item,
        for one day and since opening"""
        sold = self.stand.sales_of_menu_item_for_day(2, "Bolshevik bingsu")
        all_sold = self.stand.total_sales_for_menu_item("Bolshevik bingsu")
        self.assertEqual(sold, 3)
        self.assertEqual(all_sold, 10)

    def test_no_sales(self):
        """Tests if query for item with no sales returns string"""
        total = self.stand.sales_of_menu_item_for_day(1, "lemonade")
        self.assertIsInstance(total, str)

    def test_profit(self):
        """Tests all input sales for total item, stand profits"""
        menu = ["Das Kapital Kool-Aid", "class cake", "Bolshevik bingsu"]
        total_profit = 0
        item_profit = (3.5 - 2) * 10
        auto_item_profit = self.stand.total_profit_for_menu_item("class cake")
        auto_total_profit = self.stand.total_profit_for_stand()

        for item in menu:
            total_profit += self.stand.total_profit_for_menu_item(item)

        self.assertEqual(item_profit, auto_item_profit)
        self.assertEqual(total_profit, auto_total_profit)

if __name__ == "__main__":
    unittest.main()
