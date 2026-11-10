class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp    = [0] * (n + 1)
        if n == 0:
            return 0
        dp[1] = costs[0] + ((1 - 0) ** 2)
        if n == 1:
            return dp[1]
        dp[2] = min(
            dp[0] + costs[1] + ((2 - 0) ** 2),
            dp[1] + costs[1] + ((2 - 1) ** 2)
        )
        if n == 2:
            return dp[2]
        dp[3] = min(
            dp[0] + costs[2] + ((3 - 0) ** 2),
            min(
                dp[1] + costs[2] + ((3 - 1) ** 2),
                dp[2] + costs[2] + ((3 - 2) ** 2)
            )
        )
        for i in range(4, n + 1):
            dp[i] = min(
                dp[i - 3] + costs[i - 1] + ((i - (i - 3)) ** 2),
                min(
                    dp[i - 2] + costs[i - 1] + ((i - (i - 2)) ** 2),
                    dp[i - 1] + costs[i - 1] + ((i - (i - 1)) ** 2)
                )
            )
        return dp[-1]