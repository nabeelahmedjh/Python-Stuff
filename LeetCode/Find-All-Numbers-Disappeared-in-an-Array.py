from dis import dis
from pyparsing import nums


class Solution:
    def findDisappearedNumbers(self, nums) -> list[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct] and correct < len(nums):
                temp = nums[correct]
                nums[correct] = nums[i]
                nums[i] = temp
            else:
                i += 1

        disapeared = []
        for i in range(0, len(nums)):
            if nums[i] - 1 != i:
                disapeared.append(i + 1)

        return disapeared

    def display(self):
        print(self.findDisappearedNumbers)


def main():
    a = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(a.findDisappearedNumbers(nums))


main()
