'''
Imagine a game where you can create a zoo and start raising different types of animals. Say that for each zoo you create can have several different animals. Start by creating an Animal class, and then at least 3 specific animal classes that inherit from Animal. (Maybe lions and tigers and bears, oh my!) Each animal should at least have a name, an age, a health level, and happiness level. The Animal class should have a display_info method that shows the animal's name, health, and happiness. It should also have a feed method that increases health and happiness by 10.

In at least one of the Animal child classes you've created, add at least one unique attribute. Give each animal different default levels of health and happiness. The animals should also respond to the feed method with varying levels of changes to health and happiness.

Once you've tested out your different animals and feel more comfortable with inheritance, create a Zoo class to help manage all your animals.

One way you could put together this zoo is by doing the following:
'''


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, name, type):
        self.animals.append(animal(name, type))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


class animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display_info(self):
        print("{} is a {}!".format(self.name, self.type))


zoo1 = Zoo("John's Zoo")
zoo1.add_animal("Nala", "lion")
zoo1.add_animal("Simba", "lion")
zoo1.add_animal("Rajah", "tiger")
zoo1.add_animal("Shere Khan", "tiger")
zoo1.print_all_info()
