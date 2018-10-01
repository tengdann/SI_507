class Media:
    def __init__(self, title="No Title", author="No Author", year = "No Year"):
        self.title = title
        self.author = author
        self.year = str(year)
        
    def __str__(self):
        return self.title + ' by ' + self.author + ' (%s)' % self.year
        
    def __len__(self):
        return 0
        
class Song(Media):
    def __init__(self, title = "No Title", author = "No Author", 
                year = "No Year", album = "No Album", genre = "No Genre", track_length = 0):
        super().__init__(title, author, year)
        self.album = album
        self.genre = genre
        self.track_length = track_length
        
    def __str__(self):
        return super().__str__() + ' [%s]' % self.genre
        
    def __len__(self):
        return self.track_length
        
class Movie(Media):
    def __init__(self, title = "No Title", author = "No Author", 
                year = "No Year", rating = "No Rating", movie_length = 0):
        super().__init__(title, author, year)
        self.rating = rating
        self.movie_length = movie_length
        
    def __str__(self):
        return super().__str__() + ' [%s]' % self.rating
        
    def __len__(self):
        return self.movie_length


if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
