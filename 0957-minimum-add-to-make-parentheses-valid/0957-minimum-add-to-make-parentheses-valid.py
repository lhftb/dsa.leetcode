class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        op  = 0
        for ch in s:
            if ch == '(':
                op += 1
            else:
                if op > 0:
                    op -= 1
                else:
                    res += 1
        return res + op