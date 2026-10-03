class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stk = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    res = max(res, i - stk[-1])
        return res