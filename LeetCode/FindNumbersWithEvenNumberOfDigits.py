class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                even += 1

        return even


def main():
    s = Solution()
    nums = [12, 345, 2, 6, 7896]
    print(s.findNumbers(nums))


if __name__ == "__main__":
    main()
