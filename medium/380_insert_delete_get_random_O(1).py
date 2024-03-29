import random

class RandomizedSet:
    def __init__(self):
      self.values = set()

    def insert(self, val: int) -> bool:
      if val not in self.values:
         self.values.append(val)
         return True
      else:
       return False

    def remove(self, val: int) -> bool:
      if val in self.values:
         self.values.remove(val)
         return True
      else:
        return False

    def getRandom(self) -> int:
      return random.choice(self.values)