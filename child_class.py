from class_initialization import Human

class Superhero(Human):
    species = 'Superhuman'

    def __init__(self, movie,
    superpowers):
      self.superpowers = superpowers
      self.movie = movie
      super().__init__('tyler', 30)

    def boast(self):
      for power in self.superpowers:
          print("I wield the power of {pow}!".format(pow=power))

tyler = Superhero(True, ['strength', 'wisdom'])
print(tyler.superpowers)
tyler.boast()
print(tyler.age)