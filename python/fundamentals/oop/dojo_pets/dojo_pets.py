class pet:
    def __init__(self, name=None, type=None, tricks=None):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 20
        self.energy = 100

    def sleep(self):
        self.health += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("the pet's sound")
        return self


class ninja:
    def __init__(self, first_name, last_name, pet=pet, treats=None, pet_food=None):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet = pet
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


snorlax = pet('snorlax', 'normal')
a = ninja('John', 'Smith', snorlax)

a.feed().walk().bathe()
