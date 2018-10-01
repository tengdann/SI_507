import unittest
import proj1_f18 as proj1

class TestMedia(unittest.TestCase):
    def testConstructor(self):
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
        
    def teststr(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Kamikaze", "Eminem", 2018)
        
        self.assertEqual(str(m1), "No Title by No Author (No Year)")
        self.assertEqual(str(m2), "1999 by Prince (No Year)")
        self.assertEqual(str(m3), "Kamikaze by Eminem (2018)")
        
    def testlen(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Kamikaze", "Eminem", 2018)
        
        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 0)
        self.assertEqual(len(m3), 0)
        
class TestSong(unittest.TestCase):
    def testConstructor(self):
        pass
    
    def teststr(self):
        pass
        
    def testlen(self):
        pass


unittest.main()
