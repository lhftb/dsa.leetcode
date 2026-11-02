class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m = len(nums) // 2
        r = 0
        for i, num in enumerate(nums):
            if i != m:
                r += abs(num - nums[m])
        return r