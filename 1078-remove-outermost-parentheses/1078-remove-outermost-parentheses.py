class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cpt = 0
        beg = -1
        res = ""
        for i, ch in enumerate(s):
            if ch == '(':
                if beg == -1:
                    beg = i
                cpt += 1
            else:
                cpt -= 1
                if cpt == 0:
                    res += s[beg + 1:i]
                    beg = -1
        return res