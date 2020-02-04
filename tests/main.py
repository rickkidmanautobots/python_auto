import unittest

from art import *

from Common import shuffledeck
from Common import drawcard


class game():
    deck = shuffledeck()
    playername = ["Matt", "Carlos"]
    player1 = 0
    player2 = 0
    count = 0

    while (player1 < 3) & (player2 < 3):
        drawn = drawcard(deck)
        value1 = drawn['cards'][0]['value']
        value2 = drawn['cards'][1]['value']
        if drawn['cards'][0]['value'] == drawn['cards'][1]['value']:
            print("It's a draw!")
        elif drawn['cards'][0]['value'] > drawn['cards'][1]['value']:
            player1 += 1
        else:
            player2 += 1

        count += 1

    print("C O N G R A T U L A T I O N S ! ! After " + str(count) + " drawings:")
    if player1 > player2:
        print("The winner is:")
        tprint(playername[0], font="random")
    else:
        print("The winner is:")
        tprint(playername[1], font="random")

    print("Score Card:")
    print(playername[0] + " : " + str(player1))
    print(playername[1] + " : " + str(player2))


if __name__ == '__main__':
        game()