class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print()

book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book5 = Book("Moby-Dick", "Herman Melville", 1851)
book6 = Book("War and Peace", "Leo Tolstoy", 1869)

book4.describe()
book5.describe()
book6.describe()
