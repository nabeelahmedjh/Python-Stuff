

def main():
    fraction = get_fraction()
    print(result(fraction))


def get_fraction():
    while True:
        user_input = input("Fraction: ")
        for i in range(len(user_input)):
            if user_input[i] == "/":
                x = user_input[0: i]
                y = user_input[i + 1: len(user_input)]
                break

        try:
            x = int(x)
            y = int(y)
            if (x % 1 != 0 or y % 1 != 0 or x > y):
                continue

            return x/y*100
        except ValueError:
            print("Value Error")
        except ZeroDivisionError:
            print("Zero Division Error")


def result(fraction):
    if fraction < 1:
        return "E"
    elif fraction > 99:
        return "F"
    else:
        return str(fraction)[0: -2] + "%"


main()
