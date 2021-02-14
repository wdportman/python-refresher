from class_initialization import Human

class Superhero(Human):
    species = 'Superhuman'

    def __init__(self, movie,
    superpowers, name, age):
      self.superpowers = superpowers
      self.age = age
      self.name = name
      self.movie = movie

    def boast(self):
      for power in self.superpowers:
          print("I wield the power of {pow}!".format(pow=power))

tyler = Superhero(True, ['strength', 'wisdom'], 'tyler', 30)
print(tyler.superpowers)
tyler.boast()
print(tyler.age)