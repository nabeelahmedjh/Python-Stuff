import random


def main():
    level = getInput("Level: ")
    randomGeneratedNum = random.randrange(1, level + 1)
    print(guessNumber(randomGeneratedNum))


def isPositiveInteger(level):
    return (level.isdigit() and int(level) > 0)


def getInput(query):
    while(True):
        level = input(query)
        if (isPositiveInteger(level)):
            return int(level)


def guessNumber(randomGeneratedNum):

    while(True):
        guess = getInput("Guess: ")
        if (guess == randomGeneratedNum):
            return "Just Right!"
        elif (guess < randomGeneratedNum):
            print("Too Small!")
        elif (guess > randomGeneratedNum):
            print("Too Large!")


if __name__ == "__main__":
    main()
