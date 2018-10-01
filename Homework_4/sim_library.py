import unittest

class Library():
    def __init__(self):
        self.whole_cat = []
        self.current_cat = []
        self.out = []
        self.overdue = []
        
    def add_items(self, items):
        for item in items:
            self.whole_cat.append(item)
            self.current_cat.append(item)
            
    def __str__(self):
        catalog = "The current catalog contains: | "
        for item in self.current_cat:
            catalog += item.name + " | "
        
        return catalog
        
    def sort(self):
        self.whole_cat.sort(key = lambda x: x.name)
        self.current_cat.sort(key = lambda x: x.name)
        self.out.sort(key = lambda x: x.name)
        self.overdue.sort(key = lambda x: x.name)
            
        
class User():
    def __init__(self):
        self.current_items = []
        self.overdue_items = []
        
    def check_status(self):
        if len(self.current_items) > 0:
            items_current = "You have checked out these items: | "
            for item in self.current_items:
                items_current += item.name + " | "
            print(items_current)
        else:
            print("You have no items checked out.")
            
        if len(self.overdue_items) > 0:
            items_overdue = "These items are overdue: | "
            for item in self.overdue_items:
                items_overdue += item.name + " | "
            print(items_overdue)
        else:
            print("You have no overdue items! You are a responsible citizen of the Protectorate!")
            
    def sort(self):
        self.current_items.sort(key = lambda x: x.name)
        self.overdue_items.sort(key = lambda x: x.name)

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
            
class Text(Media): # Books, encyclopedias, newspapers, etc.
    def __init__(self, name):
        super().__init__(name, max_days = 14)
        
    def __str__(self):
        super().__str__()
        
class Audio(Media): # Purely audio component, no attached visual component
    def __init__(self, name):
        super().__init__(name, max_days = 7)
        
    def __str__(self):
        super().__str__()
        
class Digital(Media): # Refers to anything that has both an audio and visual component
    def __init__(self, name):
        super().__init__(name, max_days = 3)
        
    def __str__(self):
        super().__str__()
            
def check_overdue(Library, User):
    for item in Library.out:
        if item.days_remaining < 0:
            print(item.name, "is overdue!")
            
            Library.out.remove(item)
            Library.overdue.append(item)
            
            User.current_items.remove(item)
            User.overdue_items.append(item)
            
    Library.sort()
    User.sort()
    
def checkout(Library, Item, User):
    if Item not in Library.current_cat:
        if Item not in Library.whole_cat:
            print("Sorry, this item is not in the library.")
        else:
            print(Item)
    else:
        print(Item.name, "has been checked out!")
        Library.current_cat.remove(Item)
        Library.out.append(Item)
        User.current_items.append(Item)
        Item.checkout_status = True
        
    Library.sort()
    User.sort()
    
def return_item(Library, Item, User):
    if Item not in User.current_items and Item not in User.overdue_items:
        print("This item is not currently out.")
    elif Item in User.current_items and Item in Library.out:
        # print(Item)
        user_input = input("Would you like to return this item (Y/N)?: ")
        if user_input == 'Y':
            print("Thank you for returning this item!")
            User.current_items.remove(Item)
            Library.out.remove(Item)
            Library.current_cat.append(Item)
        elif user_input == 'N':
            print("Okay, make sure you return this item on time!")
    elif Item in User.overdue_items and Item in Library.overdue:
        print(Item)
        print("You must return this item!")
        User.overdue_items.remove(Item)
        Library.overdue.remove(Item)
        Library.current_cat.append(Item)
        print("You have returned", Item.name, ". Please do not have overdue items anymore!")
        
    Library.sort()
    User.sort()
        

def advance_day(Library, User, num_days):
    print("Advancing", num_days, "days")
    for item in Library.overdue:
        item.days_remaining -= num_days
    for item in Library.out:
        item.days_remaining -= num_days
        
    check_overdue(Library, User)
    
    Library.sort()
        
if __name__ == "__main__":
    print("Creating items...")
    book1 = Text("Art of War")
    book2 = Text("The Prince")
    book3 = Text("Magna Carta")
    audio1 = Audio("Kamikaze")
    audio2 = Audio("The Marriage of Figaro, K. 492")
    audio3 = Audio("Blue Danube")
    digital1 = Digital("The Lord of the Rings: The Fellowship of the Ring")
    digital2 = Digital("The Lord of the Rings: The Two Towers")
    digital3 = Digital("The Lord of the Rings: The Return of the King")
    print("Items created!"), print()
    
    print("Creating library...")
    library = Library()
    print("Adding items to the library...")
    library.add_items([book1, book2, book3, audio1, audio2, audio3, digital1, digital2, digital3])
    print("Library created and populated!"), print()
    
    print("Creating user...")
    user = User()
    print("User created!"), print()
    
    prompt = """What would you like to do?
    catalog: show the catalog
    checkout <item_number>
    return <item_number>
    advance <num_days>
    account: see account status, including check out items, and overdue items
    quit: exit the program\nYour choice: """
    
    user_input = str(input(prompt))
    while user_input != 'quit':
        if user_input == 'catalog':
            print(library), print()
        elif user_input.partition(' ')[0] == 'checkout':
            checkout(library, library.current_cat[int(user_input.partition(' ')[2]) - 1], user), print()
        elif user_input.partition(' ')[0] == 'return':
            return_item(library, user.current_items[int(user_input.partition(' ')[2]) - 1], user), print()
        elif user_input.partition(' ')[0] == 'advance':
            advance_day(library, user, int(user_input.partition(' ')[2])), print()
        elif user_input == 'account':
            user.check_status(), print()
        else:
            print("Input not valid, please try again"), print()
            
        user_input = str(input(prompt))
        
    print("Thank you for visiting the library, please come again!")  
        