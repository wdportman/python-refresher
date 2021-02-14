from child_class import Superhero
from another_class_definition import Bat

class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):

        Superhero.__init__(self, movie=True,
        superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'

if __name__ == '__main__':
    sup = Batman()
    # print(Batman.__mro__)
    # print(sup.get_species())
    # print(sup.sing())
    # sup.say_hi()
    # print(sup.sonar())
    # sup.age = 100
    # print(sup.age)              # => 100
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False
