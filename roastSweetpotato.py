'''
Properties:
1. cooking time
2. degree of rawness
3. seasoning
'''

'''
methods:
1. how long cooking
2. determine the rawness
3. what seasoning
'''
class RoastSweetpotato:
   def __init__(self):
       self.cook_time = 0
       self.rawness = 'raw'
       self.seasoning = []
   def roasting(self):
      while True:
        self.cook_time += int(input('How long?: '))
        if self.cook_time <= 3:
           print("cooking...done but still raw, more time need...")
           continue
        elif self.cook_time >= 8:
           self.rawness = 'overcooked'
           print(f"Cooking...done, {self.rawness}")
           break
        else:
           self.rawness = 'yummy and healthy'
           print(f"Cooking ... done, {self.rawness}!")
           break
   def __str__(self):
       return f"Cooking time: {self.cook_time}, Rawness: {self.rawness}"

test=RoastSweetpotato()

test.roasting()
print(test)









