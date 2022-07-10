

def main():
    camel = input("camelCase: ")
    print(f"snake_case: {camel_to_Snake(camel)}")


def camel_to_Snake(camel):

    snake = ""
    for i in camel:
        if (i.isupper()):
            snake += "_" + i.lower()
        else:
            snake += i

    return snake


main()
