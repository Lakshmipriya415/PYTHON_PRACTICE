
"""Object composition example 
In the example, the Book object contains Review objects inside its reviews list, which is object composition.
book
 ├── name = "Python Programming"
 └── reviews = [ r1, r2 ]
              ├── Review("Great book", 9)
              └── Review("Very helpful", 8)
"""

class Book:

    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []   # empty list for storing reviews

    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))

    def add_reviews(self, review):  
        self.reviews.append(review)


class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))


book = Book(5, "python programming", "Guido van Rossum")

review = Review(10, "Great book", 9)

book.add_reviews(review)
book.add_reviews(Review(9, "nice", 9))

print(book)

