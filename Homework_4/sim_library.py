import unittest

'''
Main class Media
- max_days, days_remaining, name, checkout_status
Subclass Book
Subclass Encyclopedia
Subclass Archival
Subclass Movies
Subclass Software
Function overdue(object)
Function checkout(object)
Function return_item(object)
Function advance_day(num_days)
'''

class Library():
    def __init__(self):
        self.whole_cat = []
        self.current_cat = []
        self.out = []
        self.overdue = []
        
class User():
    def __init__(self):
        self.current_items = []
        self.overdue_items = []
        
    def check_status(self):
        if len(self.current_items) > 0:
            print("You have checked out these items:")
            for item in self.current_items: print(item)
        else:
            print("You have overdue items, or no items checked out.")
            
        if len(self.overdue_items) > ):
            print("These items are overdue:")
            for item in self.overdue_items: print(item)
        else:
            print("You have no overdue items! You are a responsible citizen of the Protectorate!")

class Media():
    def __init__(self, name = "No stored name", max_days = 0, checkout_status = False):
        self.name = name
        self.checkout_status = checkout_status
        self.max_days = max_days
        self.days_remaining = max_days # Media in storage has same days_remaining as max_days
        
    def __str__(self):
        info = self.name + " is"
        if self.checkout_status:
            return info + " checked out; " + str(self.days_remaining) + " day(s) of " + str(self.max_days) + " remaining."
        else:
            return info + " not checked out. It can be checked out for " + str(self.max_days) + " day(s) total."
            
def check_overdue(Library):
    for item in Library.out:
        if item.days_remaining < 0:
            print(item.name, "is overdue!")
            
            Library.out.pop(item)
            Library.overdue.append(item)
    
def checkout(Library, Item):
    if Item not in Library.current_cat:
        if Item not in Library.whole_cat:
            print("Sorry, this item is not in the library.")
        else:
            print(Item)
    else:
        
    
def return_item(Library, Item):
    pass

def advance_day(Library, num_days):
    pass
            
            
class MediaTest(unittest.TestCase):
    def testinit(self):
        media = Media()
        self.assertEqual(media.name, "No stored name")
        self.assertFalse(media.checkout_status)
        self.assertEqual(media.max_days, 0)
        self.assertEqual(media.days_remaining, 0)
        
        new_media = Media("Art of War", 10, True)
        self.assertEqual(new_media.name, "Art of War")
        self.assertTrue(new_media.checkout_status)
        self.assertEqual(new_media.max_days, 10)
        self.assertEqual(new_media.days_remaining, 10)
        
    def teststr(self):
        media = Media()
        self.assertEqual(str(media), "No stored name is not checked out. It can be checked out for 0 day(s) total.")
        
        new_media = Media("Art of War", 10, True)
        self.assertEqual(str(new_media), "Art of War is checked out; 10 day(s) of 10 remaining.")
        
if __name__ == "__main__":
    unittest.main()