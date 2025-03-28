class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == "":
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

solution = Solution()
nums = list(map(int, input().split()))
target = int(input())

print(solution.search(nums, target))