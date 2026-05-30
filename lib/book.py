# book.py
# Purpose: Define a Book class for the bookstore application

class Book:
    def __init__(self, title, page_count):
        """
        Initialize a Book object with title and page_count.
        :param title: str - The title of the book
        :param page_count: int - Number of pages in the book
        """
        self.title = title
        # Validate that page_count is an integer
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            self._page_count = None

    @property
    def page_count(self):
        """
        Property to access the page count.
        Returns the number of pages if valid, else None.
        """
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """
        Set the page count if it is an integer, otherwise print an error.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """
        Simulate turning a page in the book.
        Prints a fun message to the console.
        """
        print("Flipping the page...wow, you read fast!")


# Quick test block (optional, can be removed in production)
if __name__ == "__main__":
    # Example usage
    book1 = Book("Python Basics", 200)
    print(f"Book Title: {book1.title}, Pages: {book1.page_count}")
    book1.turn_page()

    # Invalid page_count example
    book2 = Book("Bad Data Book", "two hundred")
    print(f"Book Title: {book2.title}, Pages: {book2.page_count}")
    