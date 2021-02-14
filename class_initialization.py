class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name

    def say_hi(self):
      print(f'Hello my name is {self.name}')


will = Human("will")
will.say_hi()