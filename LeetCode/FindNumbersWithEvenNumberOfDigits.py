import math


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even = 0
        for i in nums:
            digits = self.digits(i)

            if self.isEven(digits):
                even += 1

        return even

    def isEven(self, num):
        return (num % 2 == 0)

    def digits(self, num):
        if num < 0:
            num *= -1

        return (math.floor(math.log10(num)) + 1)


def main():
    s = Solution()
    nums = [12, 345, 2, 6, 7896]
    print(s.findNumbers(nums))


if __name__ == "__main__":
    main()
