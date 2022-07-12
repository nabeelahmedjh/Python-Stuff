import sys

items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    bill = 0
    while True:
        item = get_item()
        bill += get_bill(item)
        print(f"Total: ${bill}")


def get_bill(item):
    return items[item]


def get_item():
    while True:
        try:
            item = input("Item: ")
        except EOFError:
            sys.exit()

        item = item.title()
        if item not in items:
            continue

        return item


main()
