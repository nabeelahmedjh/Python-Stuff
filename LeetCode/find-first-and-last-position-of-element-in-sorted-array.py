
from turtle import up
from unicodedata import mirrored


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ans = [-1, -1]
        ans[0] = self.findBound(nums, target, False)
        ans[1] = self.findBound(nums, target, True)

        return ans

    def findBound(self, nums, target, firstOccured):
        ans = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if firstOccured:
                    ans = mid
                    start = mid + 1
                else:
                    ans = mid
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return ans


def main():
    s = Solution()
    nums = [5, 7, 7, 8, 8]
    print(s.searchRange(nums, 8))


if __name__ == "__main__":
    main()
