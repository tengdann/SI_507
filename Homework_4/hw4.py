'''
SI 507 F18 homework 4: Classes and Inheritance

Your discussion section: 003
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############ 
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10
    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state
coco = Explore_pet()
coco.hunger = 0
coco.boredom = 7
print(coco)

brian = Explore_pet("Brian")
brian.hunger = 11
brian.boredom = 0
print(brian)

#your code begins here . . . 

'''
Task B
'''
#add your codes inside of the Pet class
class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.words = ["hello"]
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"
            
    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2
        
    def say(self):
        print("I know how to say:")
        for word in self.words:
            print(word)
            
    def teach(self, word):
        self.words.append(word)
        if self.boredom < 4:
            self.boredom = 0
        else:
            self.boredom += self.boredom_decrement
            
    def feed(self):
        if self.hunger < 4:
            self.hunger = 0
        else:
            self.hunger += self.hunger_decrement
            
    def hi(self):
        x = randrange(len(self.words))
        print(self.words[x])

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

'''
Task C
'''

def teaching_session(my_pet,new_words):
    for new_word in new_words:
        my_pet.teach(new_word)
        my_pet.hi()
        status = my_pet.mood()
        print(my_pet)
        if status == "hungry":
            my_pet.feed()
        my_pet.clock_tick()
        
fido = Pet(name = "Fido")
fido.say()
teaching_session(fido, ["I am sleepy", "You are the best", "I love you, too"])
fido.say()




#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat    
'''
class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        
    def __str__(self):
        state = super().__str__()
        state.replace('.', ', arrrf!')
        return state
        
class Cat(Pet):
    def __init__(self, name, meow_count = 0):
        super().__init__(name)
        self.meow_count = meow_count
        
    def hi(self):
        x = randrange(len(self.words))
        print(self.words[x]*self.meow_count)

'''
Task B: Poodle 
'''
class Poodle(Dog):
    def __init__(self, name):
        super().__init__(name)
        
    def dance(self):
        print("Dancing in circles like poodles do!")
        
    def say(self):
        self.dance()
        super().say()
        
puppers = Poodle("Puppers")
puppers.say()

meowington = Cat("Meowington", meow_count = 7)
meowington.hi()





