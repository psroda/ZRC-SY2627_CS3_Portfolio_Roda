
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.__pages = 1
        self.set_pages(pages)

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__pages)


class Magazine(Publication):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.__issue = 1
        self.set_issue(issue)

    def get_issue(self):
        return self.__issue

    def set_issue(self, issue):
        if issue > 0:
            self.__issue = issue
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue number:", self.__issue)


# Create two Publication objects
p1 = Publication("Science Today", "Anna Cruz")
p2 = Publication("Young Readers", "Mark Santos")

# Create two Book objects
b1 = Book("The Lost Island", "Mia Reyes", 250)
b2 = Book("Beyond the Stars", "Leo Garcia", 180)

# Create two Magazine objects
m1 = Magazine("Tech Monthly", "Ella Diaz", 5)
m2 = Magazine("Nature Journal", "Noah Lim", 8)


print("PUBLICATIONS")
p1.display_info()
print()
p2.display_info()

print("\nBOOKS")
b1.display_info()
print()
b2.display_info()

print("\nMAGAZINES")
m1.display_info()
print()
m2.display_info()
