from datetime import date, datetime, timedelta
import sys
import inflect

p = inflect.engine()


def main():
    now = date.today()
    dateOfBirth = getDoB()

    duration = now - dateOfBirth
    duration_in_minutes = formatDuration(duration)

    print(duration_in_minutes)


def getDoB():
    userInput = input("Date of Birth: ")

    userInput = validate(userInput)
    try:
        dateOfBirth = date(int(userInput[0]), int(
            userInput[1]), int(userInput[2]))

    except Exception:
        print("invalid date")
        sys.exit()

    return dateOfBirth


def validate(userInput):
    if not('-' in userInput):
        print("Invalid date")
        sys.exit()

    userInput = userInput.split("-")

    if len(userInput) != 3:
        print("Invalid date")
        sys.exit()

    for item in userInput:
        if not(item.isnumeric()):
            print("Invalid date")
            sys.exit()

    return userInput


def formatDuration(duration):
    duration_in_minutes = round((duration.total_seconds() / 60))

    return (p.number_to_words(
        duration_in_minutes) + " minutes").replace(" and", "").capitalize()


if __name__ == "__main__":
    main()
