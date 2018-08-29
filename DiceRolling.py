# Imports random library
import random

# Global Constants
MAX = 6
MIN = 1

def main():
    answer=random.randint(MIN,MAX)
    print("The dice rolled",answer)
    goagain = input("Would you like to roll the dice again? (Y/N) ")
    while goagain == "Y" or goagain == "y":
        answer=random.randint(MIN,MAX)
        print("The dice rolled",answer)
        goagain = input("Would you like to roll the dice again? (Y/N) ")

    if goagain == "N" or goagain == "n":
        print("Thank you for playing, come again.")

main()


