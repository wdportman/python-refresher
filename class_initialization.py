class Human:
    species = "H. sapiens"

    @classmethod
    def get_species(cls):
      return cls.species

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
      print(f'Hello my name is {self.name} and my age is {self.age}.')


will = Human("will", 29)