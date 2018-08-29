import random

def pickdice():
    continueprompting = True
    dicetype = 0

    #Errors
    while continueprompting:
        dicetype = int(input("How many sides does your dice have? "))
        if not (dicetype in [4,6,8,10,12,20]):
            print("Invalid amount of sides, choices are 4, 6, 8, 10, 12, and 20")
        else:
            continueprompting = False

    #Assigns min and max numbers for dice to roll
    if dicetype == 4:
        maximum = 4
        minimum = 1
    if dicetype == 6:
        maximum = 6
        minimum = 1
    if dicetype == 8:
        maximum = 8
        minimum = 1
    if dicetype == 10:
        maximum = 10
        minimum = 1
    if dicetype == 12:
        maximum = 12
        minimum = 1
    if dicetype == 20:
        maximum = 20
        minimum = 1

    #Returns max and mins
    return maximum,minimum

def rolldice(maximum, minimum):
    maxnum = maximum
    minnum = minimum
    print("Rolling the dice...")
    dicevalue = random.randint(minnum,maxnum)
    print("The dice rolled a",dicevalue)
    rollagain = input("Would you like to roll again? ")
    while rollagain == "Y" or rollagain == "y":
        print("Rolling the dice...")
        dicevalue = random.randint(minnum,maxnum)
        print("The dice rolled a",dicevalue)
        rollagain = input("Would you like to roll again? ")
    if rollagain == "N" or rollagain == "n":
        print("Thank you for using this program! Goodbye!")
    while rollagain not in ["N","n","Y","y"]:
        print("Invalid answer...")
        rollagain = input("Would you like to roll again? ")

def main():
    maximum, minimum = pickdice()
    rolldice(maximum,minimum)

main()
