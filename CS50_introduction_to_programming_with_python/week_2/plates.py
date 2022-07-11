def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = True
    if len(s) > 6 and len(s) < 2:
        return False

    if not(s[0].isalpha() and s[1].isalpha()):
        return False

    if not(s[len(s) - 1].isnumeric()):
        return False

    for i in s:
        num_count = 0

        if (i == '0' and num_count == 0):
            valid = False
            break

        if (i in [".", ",", "!"]):
            valid = False

        if (i.isnumeric()):
            num_count += 1

    return valid


main()
