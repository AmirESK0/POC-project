# magic methods = dunder methods (double underscore) __init__, __str__, __eq__
#                 they are automatically called by many of python's built-in operations
#                 they allow developers to define or customize the behavior of objects


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # How the object is shown when printed
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Equality: same title AND same author
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # Comparisons based on number of pages
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # Add books → total pages
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # "in" keyword support
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages



book1 = Book("the Hobbit", "J.J.R. Tolkien", 310)
book2 = Book("the Hobbit", "J.J.R. Tolkien", 311)
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)


print(book1)
print(book1 == book2)
print(book2 < book3)
print(book2 > book3)
print(book2 + book3)
print("Lion" in book4)
print(book3["title"])
print(book3["num_pages"])

