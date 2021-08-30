from classes.deck import Deck
# card game will keep draw a card for user and host and compare each time in one deck

# the user draws the card first and then the host draws the card, and they will compare their card, higher points of the card is the winner of the round, points is not accumulatively counted


def newGame():
    deck = Deck()
    deck.draw_card()
    while deck.hasCard():
        user_input = input("Keep Playing? y/n ")
        if user_input == "n" or user_input == "no":
            break
        elif user_input == "y" or user_input == "yes":
            deck.draw_card()
        else:
            print("I don't understand, please try again.")


while True:
    play = input("New Game? y/n ")
    if play == "n" or play == "no":
        print("Bye Bye!")
        break
    elif play == "y" or play == "yes":
        newGame()
    else:
        print("I don't understand, please try again.")
