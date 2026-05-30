# coffee.py
# Purpose: Define a Coffee class for the bookstore application

class Coffee:
    def __init__(self, size, price):
        """
        Initialize a Coffee object with size and price.
        :param size: str - Coffee size (Small, Medium, Large)
        :param price: float - Price of the coffee
        """
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")
            self._size = None
        self.price = price

    @property
    def size(self):
        """Return the size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size if it is one of the allowed options, otherwise print an error."""
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Simulate tipping for the coffee and increase price by 1."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
