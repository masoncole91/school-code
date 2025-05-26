"""
Mason Blanford
Oct. 4, 2022
Records menu items and daily sales of a lemonade stand
"""

# pylint: disable = invalid-name

class LemonadeStand:
    """Transacts, records daily lemonade stand sales"""
    def __init__(self, name):
        self._name = name
        self._current_day = 1
        self._menu_dict = {}
        self._sales_record = []

    def add_menu_item(self, menu_item):
        """Adds menu object to menu dictionary"""
        name = MenuItem.get_name(menu_item)
        wholesale_cost = MenuItem.get_wholesale_cost(menu_item)
        selling_price = MenuItem.get_selling_price(menu_item)
        self._menu_dict.setdefault(name, MenuItem(name, wholesale_cost, selling_price))

    def enter_sales_for_today(self, items_sold):
        """Registers a day's sales,
         Raises current day by one"""
        def log_sales():
            log = SalesForDay(self._current_day, items_sold)
            self._sales_record += [log]
            self._current_day += 1
            for item in items_sold:
                if item not in self._menu_dict:
                    raise InvalidSalesItemError
        try:
            log_sales()
        except InvalidSalesItemError:
            print("A listed item isn't sold here.")

    def sales_of_menu_item_for_day(self, day, item):
        """Returns amount of item sold on given day"""
        for log in self._sales_record:
            logged_day = SalesForDay.get_day(log)
            logged_sales = SalesForDay.get_sales_dict(log)
            if day == logged_day:
                if item in logged_sales:
                    return logged_sales[item]
        return "There were no sales of this item on this day."

    def total_sales_for_menu_item(self, name):
        """Returns total amount of item sold since the stand's opening"""
        total_sold = 0
        for log in self._sales_record:
            logged_sales = SalesForDay.get_sales_dict(log)
            if name in logged_sales:
                total_sold += logged_sales[name]
        return total_sold

    def total_profit_for_menu_item(self, name):
        """Returns total profit for item since stand's opening,
        by sales price minus wholesale cost"""
        profit = 0
        for item, val in self._menu_dict.items():
            if name == item:
                wholesale = MenuItem.get_wholesale_cost(val)
                sale = MenuItem.get_selling_price(val)
                profit = sale - wholesale
                profit = profit * self.total_sales_for_menu_item(name)
        return profit

    def total_profit_for_stand(self):
        """Returns total profit of lemonade stand since opening"""
        all_profit = 0
        for name in self._menu_dict:
            all_profit += self.total_profit_for_menu_item(name)
        return all_profit

    def get_name(self):
        """Accesses name of lemonade stand as string"""
        return self._name

    def get_menu(self):
        """Accesses menu dictionary:
        key = name of item
        value = MenuItem object"""
        return self._menu_dict

    def get_current_day(self):
        """Accesses integer as current day"""
        return self._current_day

    def get_sales_record(self):
        """Accesses sales record list"""
        return self._sales_record

class SalesForDay:
    """Stores sales for particular day at lemonade stand"""
    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Accesses integer for total days since stand's opening"""
        return self._day

    def get_sales_dict(self):
        """Accesses dictionary,
        key = item sold
        value = amount of items sold that day"""
        return self._sales_dict

class MenuItem:
    """Stores menu objects for customer purchase"""
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Accesses string for name of sold item"""
        return self._name

    def get_wholesale_cost(self):
        """Accesses float for amount item is bought by lemonade stand"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Accesses float for amount lemonade stand sells an item"""
        return self._selling_price

class InvalidSalesItemError(Exception):
    """Raises error when invalid item is sold"""

def main():
    """Checks if script is imported,
    If not, run"""
    if __name__ == "__main__":
        stand = LemonadeStand("Liz Lemon's Lucrative Lemons")
        item1 = MenuItem("lemon cake", 1.0, 20.0)
        item2 = MenuItem("lemon steak", 5.0, 50.0)
        item3 = MenuItem("lemonade", 0.5, 15.0)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        stand.add_menu_item(item3)
        day_one_sales = {"lemon cake": 50.0,
                         "lemon steak": 5.0,
                         "lemon salad": 2.0}
        stand.enter_sales_for_today(day_one_sales)

main()
