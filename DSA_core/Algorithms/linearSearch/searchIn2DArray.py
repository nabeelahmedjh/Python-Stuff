
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

    def findMinimun(self, array):
        if len(array) == 0:
            return False
        min = array[0][0]
        for i in range(0, len(array)):
            for j in range(0, len(array[i])):
                if min > array[i][j]:
                    min = array[i][j]

        return min

    def findMaximun(self, array):
        if len(array) == 0:
            return False
        max = array[0][0]
        for i in range(0, len(array)):
            for j in range(0, len(array[i])):
                if max < array[i][j]:
                    max = array[i][j]

        return max


def main():
    l = LinearSearch2D()
    array = [[4, 2, 54, 56], [23, 54, 2, 6], [-1, 54, 76, 12, 65]]
    print(l.searchLinear(array, 65))
    print(l.findMinimun(array))
    print(l.findMaximun(array))


if __name__ == "__main__":
    main()
