

def main():
    user_input = input("Input: ")

    print(reduce(user_input))


def reduce(user_input):
    reduced_str = ""
    for i in user_input:
        if (i.lower() not in ["a", "e", "i", "o", "u"]):
            reduced_str += i

    return reduced_str


if __name__ == "__main__":
    main()
