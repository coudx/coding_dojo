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


snorlax = pet('snorlax', 'normal')


class subpet(pet):
    def __init__(self):
        pass
