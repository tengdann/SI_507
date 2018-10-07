import json
import requests
import webbrowser
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

base_itunes_url = "https://itunes.apple.com/search?"

# Caching code
CACHE_FNAME = "itunes_cache.json"
try:
    with open(CACHE_FNAME,'r') as cache_file:
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        
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
        
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(baseurl, params)
        try:
            CACHE_DICTION[unique_ident] = json.loads(resp.text)
            dumped_json_cache = json.dumps(CACHE_DICTION, indent = 4)
            fw = open(CACHE_FNAME, "w")
            fw.write(dumped_json_cache)
            fw.close()
            return CACHE_DICTION[unique_ident]
        except:
            print("Error, search term returned NullResponse")
            return
        
def get_requests_from_itunes(param1_type = None, param1_term = None, param2_type = None, param2_term = None, param3_type = None, param3_term = None):
    params_diction = {}
    if param1_type is not None and param1_term is not None:
        params_diction[param1_type] = param1_term.replace(' ', '+')
        
    if param2_type is not None and param2_term is not None:
        params_diction[param2_type] = param2_term
        
    if param3_type is not None and param3_term is not None:
        params_diction[param3_type] = param3_term
        
    return make_request_using_cache(base_itunes_url, params_diction)

# Default param1_type = term, param2_type = limit, param3_type = None
# Returns a list of media types
def create_media_types_from_itunes(param1_term = None, param2_term = None):
    returned_medias = []
    json_request = get_requests_from_itunes(param1_type = "term", param1_term = param1_term, param2_type = "limit", param2_term = param2_term)
    
    try:
        for single_request in json_request['results']:
            try:
                if single_request['kind'] == "song":
                    returned_medias.append(Song(json = single_request))
                elif single_request['kind'] == "feature-movie":
                    returned_medias.append(Movie(json = single_request))
                else: # In case its like a music-video or something...
                    returned_medias.append(Media(json = single_request))
            except: # For everything without key 'kind'
                returned_medias.append(Media(json = single_request))
    except:
        pass

    return returned_medias
    
class Media:
    def __init__(self, title = "No Title", author = "No Author", year = "No Year", json = None):
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
            try:
                self.url = json["trackViewUrl"]
            except:
                self.url = json["collectionViewUrl"]
        
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

if __name__ == "__main__":
    term = input("Enter a search term, or \"quit\" to quit: ")
    while term != "quit":
        index = 1
        master_list = create_media_types_from_itunes(param1_term = term)
        indexed_list = []
        song_list = []
        movie_list = []
        other_list = []
        if len(master_list) != 0:
            for item in master_list:
                if type(item) == type(Song()):
                    song_list.append(item)
                elif type(item) == type(Movie()):
                    movie_list.append(item)
                else:
                    other_list.append(item)
            
            print()
            if len(song_list) != 0:
                print("SONGS")
                for song in song_list:
                    print(index, song)
                    index += 1
                    indexed_list.append(song)
                print()
            else:
                print("No song found!"), print()
            
            if len(movie_list) != 0:
                print("MOVIES")
                for movie in movie_list:
                    print(index, movie)
                    index += 1
                    indexed_list.append(movie)
                print()
            else:
                print("No movies found!"), print()
            
            if len(other_list) != 0:
                print("OTHER MEDIA")
                for other in other_list:
                    print(index, other)
                    index += 1
                    indexed_list.append(other)
                print()
            else:
                print("No other media types found!"), print()
        
            term = input("Enter a number for more info, or another search term, or quit: ")
        
            while True:
                try:
                    while int(term) > len(indexed_list):
                        print("Sorry, that is out of range!"), print()
                        term = input("Enter a number for more info, or another search term, or quit: ")
                    
                    print("Launching", indexed_list[int(term) - 1].url, "in web browser..."), print()
                    webbrowser.open(indexed_list[int(term) - 1].url)
                    term = input("Enter a number for more info, or another search term, or quit: ")
                except:
                    break
                
        else:
            print("No results for this query!")
            term = input("Enter a search term, or \"quit\" to quit: ")