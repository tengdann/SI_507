import win32com.client as wincl
TTS = wincl.Dispatch("SAPI.SpVoice")

class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs

  def greeting(self):
    return "cowers"
    
  def speak(self):
    return "..."

class Dog(Animal):
  breed = ''

  def __init__(self, nm, br):
    super().__init__(nm)
    self.breed = br

  def greeting(self):
    return "wags"
    
  def speak(self):
    return "woof"

class Cow(Animal):
  pass
  
  def speak(self):
    return "mooooooooo"

class Bird(Animal):
  legs = 2
  
  def speak(self):
    return "Avast ye landlubbers"

class Spider(Animal):
  legs = 8
  
  def speak(self):
    return "spiders can't talk, silly"
    
class Snake(Animal):
    legs = 0
    
    def greeting(self):
        return "slithers"
        
    def speak(self):
        return "hiss"

d1 = Dog('Fido',  'Dachsund')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')
sn1 = Snake('Nagini')

animals = [d1, c1, b1, s1, sn1]
# for a in animals:
    # TTS.Speak(a.name + 'has' + str(a.get_num_legs()) + 'legs and' + a.greeting())
  
for a in animals:
    print(a.name + ' says ' + a.speak())
    TTS.Speak(a.name + ' says ' + a.speak())