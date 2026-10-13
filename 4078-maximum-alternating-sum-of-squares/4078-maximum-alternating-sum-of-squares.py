class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        m = 0
        i = 0
        j = len(nums) - 1
        nums.sort(reverse=True)
        n = len(nums) // 2
        if (len(nums) % 2) == 1:
            n += 1
        for k in range(n):
            if abs(nums[i]) > abs(nums[j]):
                m += (nums[i] ** 2)
                i += 1
            else:
                m += (nums[j] ** 2)
                j -= 1
        while i <= j:
            m -= (nums[i] ** 2)
            i += 1
        return m