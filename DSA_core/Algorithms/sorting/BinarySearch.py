

def main():
    nums = [1, 3]
    print(binarySearch(nums, 2))


def binarySearch(nums, value):
    start = 0
    last = len(nums) - 1

    while start <= last:
        mid = (start + last) // 2

        if nums[mid] == value:
            return mid
        elif nums[mid] > value:
            last = mid - 1
        elif nums[mid] < value:
            start = mid + 1

    return None


if __name__ == "__main__":
    main()
