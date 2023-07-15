import csv
import os
import sys


class Item:
    """Description"""

    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        """Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        print(f"An instance created for {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        """Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        return self.price * self.quantity

    def apply_discount(self):
        """Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open(os.path.join(sys.path[0], "items.csv"), "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item["name"],
                price=float(item["price"]),
                quantity=int(item["quantity"])
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        if isinstance(num, int):
            return True
        return False


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

Item.instantiate_from_csv()
print(Item.all)
