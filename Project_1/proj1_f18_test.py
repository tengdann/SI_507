import unittest
import proj1_f18 as proj1
import json

class TestMedia(unittest.TestCase):
    def test_Mediaa_Constructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Kamikaze", "Eminem", 2018)

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.year, "No Year")
        self.assertFalse(hasattr(m1, "rating"))
        self.assertFalse(hasattr(m1, "genre"))
        self.assertFalse(hasattr(m1, "album"))
        
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.year, "No Year")
        self.assertFalse(hasattr(m2, "rating"))
        self.assertFalse(hasattr(m2, "genre"))
        self.assertFalse(hasattr(m2, "album"))
        
        self.assertEqual(m3.title, "Kamikaze")
        self.assertEqual(m3.author, "Eminem")
        self.assertEqual(m3.year, "2018")
        self.assertFalse(hasattr(m3, "rating"))
        self.assertFalse(hasattr(m3, "genre"))
        self.assertFalse(hasattr(m3, "album"))
        
    def test_Media_str(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Kamikaze", "Eminem", 2018)
        
        self.assertEqual(str(m1), "No Title by No Author (No Year)")
        self.assertEqual(str(m2), "1999 by Prince (No Year)")
        self.assertEqual(str(m3), "Kamikaze by Eminem (2018)")
        
    def test_Media_len(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Kamikaze", "Eminem", 2018)
        
        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 0)
        self.assertEqual(len(m3), 0)

        
class TestSong(unittest.TestCase):
    def test_Song_Constructor(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Kamikaze", "Eminem", 2018, "Kamikaze", "Rap", 216 * 1000)
        s3 = proj1.Song("Blue Danube", "Johann Strauss II", 1866)
        
        self.assertEqual(s1.album, "No Album")
        self.assertEqual(s1.genre, "No Genre")
        self.assertEqual(s1.track_length, 0)
        self.assertFalse(hasattr(s1, "rating"))
        
        self.assertEqual(s2.album, "Kamikaze")
        self.assertEqual(s2.genre, "Rap")
        self.assertEqual(s2.track_length, 216000)
        self.assertFalse(hasattr(s2, "rating"))
        
        self.assertEqual(s3.album, "No Album")
        self.assertEqual(s3.genre, "No Genre")
        self.assertEqual(s3.track_length, 0)
        self.assertFalse(hasattr(s3, "rating"))
    
    def test_Song_str(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Kamikaze", "Eminem", 2018, "Kamikaze", "Rap", 216 * 1000)
        s3 = proj1.Song("Blue Danube", "Johann Strauss II", 1866)
        
        self.assertEqual(str(s1), "No Title by No Author (No Year) [No Genre]")
        self.assertEqual(str(s2), "Kamikaze by Eminem (2018) [Rap]")
        self.assertEqual(str(s3), "Blue Danube by Johann Strauss II (1866) [No Genre]")
        
    def test_Song_len(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Kamikaze", "Eminem", 2018, "Kamikaze", "Rap", 216 * 1000)
        s3 = proj1.Song("Blue Danube", "Johann Strauss II", 1866)
        
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 216000)
        self.assertEqual(len(s3), 0)

        
class TestMovie(unittest.TestCase):
    def test_Movie_Constructor(self):
        mv1 = proj1.Movie()
        mv2 = proj1.Movie("Armageddon", "Michael Bay", 1998)
        mv3 = proj1.Movie("The Lord of the Rings: The Two Towers", "Peter Jackson", 2002, "PG-13", 179 * 60 * 1000)
        
        self.assertEqual(mv1.rating, "No Rating")
        self.assertEqual(mv1.movie_length, 0.0)
        self.assertFalse(hasattr(mv1, "genre"))
        self.assertFalse(hasattr(mv1, "album"))
        
        self.assertEqual(mv2.title, "Armageddon")
        self.assertEqual(mv2.author, "Michael Bay")
        self.assertEqual(mv2.year, "1998")
        self.assertFalse(hasattr(mv2, "genre"))
        self.assertFalse(hasattr(mv2, "album"))
        
        self.assertEqual(mv3.rating, "PG-13")
        self.assertEqual(mv3.movie_length, 179 * 60 * 1000)
        self.assertFalse(hasattr(mv3, "genre"))
        self.assertFalse(hasattr(mv3, "album"))
    
    def test_Movie_str(self):
        mv1 = proj1.Movie()
        mv2 = proj1.Movie("Armageddon", "Michael Bay", 1998)
        mv3 = proj1.Movie("The Lord of the Rings: The Two Towers", "Peter Jackson", 2002, "PG-13", 179 * 60 * 1000)
        
        self.assertEqual(str(mv1), "No Title by No Author (No Year) [No Rating]")
        self.assertEqual(str(mv2), "Armageddon by Michael Bay (1998) [No Rating]")
        self.assertEqual(str(mv3), "The Lord of the Rings: The Two Towers by Peter Jackson (2002) [PG-13]")
        
    def test_Movie_len(self):
        mv1 = proj1.Movie()
        mv2 = proj1.Movie("Armageddon", "Michael Bay", 1998)
        mv3 = proj1.Movie("The Lord of the Rings: The Two Towers", "Peter Jackson", 2002, "PG-13", 179 * 60 * 1000)
        
        self.assertEqual(len(mv1), 0)
        self.assertEqual(len(mv2), 0)
        self.assertEqual(len(mv3), 179 * 60 * 1000)
        
file = open('sample_json.json', 'r')
sample_json = json.loads(file.read())
file.close()
        
class TestJson(unittest.TestCase):  
    def test_Media_json(self):
        m1 = proj1.Media(json = sample_json[2])
        
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.year, "2012")
        
        self.assertEqual(str(m1), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(len(m1), 0)
        
    def test_Song_json(self):
        s1 = proj1.Song(json = sample_json[1])
        
        self.assertEqual(s1.title, "Hey Jude")
        self.assertEqual(s1.author, "The Beatles")
        self.assertEqual(s1.year, "1968")
        self.assertEqual(s1.album, "The Beatles 1967-1970 (The Blue Album)")
        self.assertEqual(s1.genre, "Rock")
        
        self.assertEqual(str(s1), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(len(s1), 431333)
        
    def test_Movie_json(self):
        mv1 = proj1.Movie(json = sample_json[0])
        
        self.assertEqual(mv1.title, "Jaws")
        self.assertEqual(mv1.author, "Steven Spielberg")
        self.assertEqual(mv1.year, "1975")
        self.assertEqual(mv1.rating, "PG")
        
        self.assertEqual(str(mv1), "Jaws by Steven Spielberg (1975) [PG]")
        self.assertEqual(len(mv1), 7451455)

unittest.main(verbosity = 2)
