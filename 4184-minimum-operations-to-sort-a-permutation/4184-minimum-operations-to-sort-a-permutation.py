class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(0)
        asc = True
        desc = True
        for j in range(1, n):
            v = nums[(i + j) % n]
            if v != j:
                asc = False
            if v != (n - j):
                desc = False
            if not asc and not desc:
                return -1
        return min(i, n - i + 2) if asc else min(n - i, i + 2)