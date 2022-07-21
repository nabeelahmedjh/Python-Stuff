

def missingNumber(nums) -> int:
    i = 0
    while i < len(nums) - 1:
        print(len(nums))
        if nums[i] != i and not(nums[i] >= len(nums)):
            temp = nums[i]
            nums[i] = nums[nums[i]]
            nums[temp] = temp
            continue
        i += 1

    print(nums)


def main():
    nums = [1, 3, 4, 0]
    missingNumber(nums)


main()
