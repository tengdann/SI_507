import requests
import json

class Media:
    def __init__(self, title="No Title", author="No Author", year = "No Year", json = None):
        if json is None:
            self.title = title
            self.author = author
            self.year = str(year)
        else:
            try:
                self.title = json["trackName"]
            except:
                self.title = json["collectionName"]
                
            self.author = json["artistName"]
            self.year = json["releaseDate"].split('-')[0]
        
    def __str__(self):
        return self.title + ' by ' + self.author + ' (%s)' % self.year
        
    def __len__(self):
        return 0
        
class Song(Media):
    def __init__(self, title = "No Title", author = "No Author", 
                year = "No Year", album = "No Album", genre = "No Genre", track_length = 0, json = None):
        if json is None:
            super().__init__(title, author, year)
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            super().__init__(json = json)
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = json["trackTimeMillis"]
        
    def __str__(self):
        return super().__str__() + ' [%s]' % self.genre
        
    def __len__(self):
        return self.track_length # Return to the nearest millisecond, as per JSON file
        
class Movie(Media):
    def __init__(self, title = "No Title", author = "No Author", 
                year = "No Year", rating = "No Rating", movie_length = 0, json = None):
        if json is None:
            super().__init__(title, author, year)
            self.rating = rating
            self.movie_length = movie_length
        else:
            super().__init__(json = json)
            self.rating = json["contentAdvisoryRating"]
            self.movie_length = json["trackTimeMillis"]
        
    def __str__(self):
        return super().__str__() + ' [%s]' % self.rating
        
    def __len__(self):
        return self.movie_length # Return to the nearest millisecond, as per JSON file

# Caching code
CACHE_FNAME = "itunes_cache.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}
    
def params_unique_comb(baseurl, params):
    alphabetized_keys = sorted(params.keys())
    res = []
    
    for k in alphabetized_keys:
        res.append("{}-{}".format(k, params[k]))
    
    return baseurl +"_"+"_".join(res)
    
def make_request_using_cache(baseurl, params):
    unique_ident = params_unique_comb(baseurl, params)
    
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
        
    # FINISH THIS

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
