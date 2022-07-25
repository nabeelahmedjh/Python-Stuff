
class LinearSearch2D:
    def __init__(self) -> None:
        pass

    def searchLinear(self, array, target):

        if len(array) == 0:
            return False
        for i in range(0, len(array)):
            for j in range(0, len(array[i])):
                if array[i][j] == target:
                    return f" at [{i}][{j}]"

        return False


def main():
    l = LinearSearch2D()
    array = [[4, 2, 54, 56], [23, 54, 2, 6], [-1, 54, 76, 12, 65]]
    print(l.searchLinear(array, 65))


if __name__ == "__main__":
    main()
