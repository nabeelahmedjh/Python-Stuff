

def main():
    l = [2, 5, 3, 4, 1]
    print(l)
    l = cyclesort(l)
    print(l)


def cyclesort(l):
    i = 0
    while i < len(l) - 1:
        if l[i] != i + 1:
            temp = l[l[i] - 1]
            l[l[i] - 1] = l[i]
            l[i] = temp

            continue
        i += 1

    return l


main()
