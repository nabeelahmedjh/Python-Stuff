class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        last = len(nums) - 1
        while start <= last:
            mid = (start + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                last = mid - 1

        return -1


def main():
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    print(s.search(nums, 13))


main()
