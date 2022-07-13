import sys


def main():
    grocery = {}
    add_grocery(grocery)
    grocery = sort_grocery(grocery)
    print_grocery(grocery)


def add_grocery(grocery):
    while True:
        try:
            item = input()
        except EOFError:
            return 0

        if item.upper() not in grocery:
            grocery[item.upper()] = 0

        grocery[item.upper()] += 1


def sort_grocery(grocery):
    keys = sorted(grocery)
    sorted_grocery = {}

    for key in keys:
        sorted_grocery[key] = grocery[key]

    return sorted_grocery


def print_grocery(grocery):

    for item in grocery:
        print(f"{grocery[item]} {item}")


main()
