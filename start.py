import random
intMysteryNumber=random.randint(0,100)
for intCounter in range(100):
    intGuess=int(input("Guess the number: "))
    if intGuess == intMysteryNumber:
        print("You are a genius")
        break;
    if intMysteryNumber > intGuess:
        print("The number is higher")
    else:
        print("The number is lower")