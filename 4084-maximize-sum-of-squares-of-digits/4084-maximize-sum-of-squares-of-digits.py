class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = []
        while sum > 0 and len(res) < num:
            res.append(str(min(9, sum)))
            sum -= min(9, sum)
        if sum > 0 or len(res) > num:
            return ""
        while len(res) < num:
            res.append('0')
        return "".join(res)