import unittest
import proj1_f18 as proj1

class TestMedia(unittest.TestCase):
    def test_Mediaa_Constructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Kamikaze", "Eminem", 2018)

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.year, "No Year")
        
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.year, "No Year")
        
        self.assertEqual(m3.title, "Kamikaze")
        self.assertEqual(m3.author, "Eminem")
        self.assertEqual(m3.year, "2018")
        
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
        s2 = proj1.Song("Kamikaze", "Eminem", 2018, "Kamikaze", "Rap", 180 + 36)
        s3 = proj1.Song("Blue Danube", "Johann Strauss II", 1866)
        
        self.assertEqual(s1.album, "No Album")
        self.assertEqual(s1.genre, "No Genre")
        self.assertEqual(s1.track_length, 0)
        
        self.assertEqual(s2.album, "Kamikaze")
        self.assertEqual(s2.genre, "Rap")
        self.assertEqual(s2.track_length, 216)
        
        self.assertEqual(s3.album, "No Album")
        self.assertEqual(s3.genre, "No Genre")
        self.assertEqual(s3.track_length, 0)
    
    def test_Song_str(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Kamikaze", "Eminem", 2018, "Kamikaze", "Rap", 180 + 36)
        s3 = proj1.Song("Blue Danube", "Johann Strauss II", 1866)
        
        self.assertEqual(str(s1), "No Title by No Author (No Year) [No Genre]")
        self.assertEqual(str(s2), "Kamikaze by Eminem (2018) [Rap]")
        self.assertEqual(str(s3), "Blue Danube by Johann Strauss II (1866) [No Genre]")
        
    def test_Song_len(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Kamikaze", "Eminem", 2018, "Kamikaze", "Rap", 180 + 36)
        s3 = proj1.Song("Blue Danube", "Johann Strauss II", 1866)
        
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 216)
        self.assertEqual(len(s3), 0)

        
class TestMovie(unittest.TestCase):
    def test_Movie_Constructor(self):
        mv1 = proj1.Movie()
        mv2 = proj1.Movie("Armageddon", "Michael Bay", 1998)
        mv3 = proj1.Movie()
    
    def test_Movie_str(self):
        pass
        
    def test_Movie_len(self):
        pass

unittest.main(verbosity = 2)
