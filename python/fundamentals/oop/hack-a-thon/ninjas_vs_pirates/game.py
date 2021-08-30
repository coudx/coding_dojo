from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

while jack_sparrow.health > 0 and michelangelo.health > 0:
    michelangelo.attack(jack_sparrow)
    jack_sparrow.show_stats()
    jack_sparrow.attack(michelangelo)
    michelangelo.show_stats()

print("Battle End!")
if jack_sparrow.health > 0:
    print("Pirate win!")
else:
    print("Ninja Win!")
