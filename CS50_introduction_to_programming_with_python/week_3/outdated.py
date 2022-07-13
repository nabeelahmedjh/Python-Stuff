import re
import sys


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    date = get_date(months)
    print(date)
    print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")


def get_date(months):
    while True:
        try:
            date = input("Date: ")
        except EOFError or KeyboardInterrupt:
            sys.exit()
        date = re.split(", |/| ", date)

        if len(date) != 3:
            continue

        if date[0].isalpha():
            if date[0].title() not in months:
                continue
            else:
                date[0] = months.index(date[0].title()) + 1
        elif date[0].isnumeric() and (int(date[0]) > 12 or int(date[0]) < 1):
            continue

        try:
            if int(date[1]) > 31 or int(date[1]) < 1 or int(date[2]) < 1:
                continue
        except KeyError:
            continue

        return date


main()
