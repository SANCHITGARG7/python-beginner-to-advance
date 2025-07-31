import random

score =10
randomNumber = random.randint(1,10)

while True:
    userInput = int(input('Guess :'))


    if userInput == randomNumber:
        print("congrats you won")
        break

    else:
        print('better luck next time')
        score -=1