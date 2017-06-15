class Bookstore(object):
    def __init__(self,name):
        self.name = name
        self.bookstore = []
    
    def add_book(self,book):
        self.bookstore.append(book)
        
    def get_books(self):
        return self.bookstore
    
    def search_books(self,title=None,author=None):
        search_result = []
        for query in self.bookstore:
            if title == None:
                if author.name.lower() in query.author.name.lower():
                    search_result.append(query)
            elif author == None:        
                if title.lower() in query.title.lower():
                    search_result.append(query)
            else: 
                if author.lower() in query.author.name.lower() and title.lower() in query.title.lower():
                    search_result.append(query)
        return search_result

class Author(object):
    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality
        self.books = []

    def get_books(self):
        return self.books

class Book(object):
    def __init__(self,title,author):
        self.title = title
        self.author = author
        author.books.append(self)
