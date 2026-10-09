class Solution:
    def minInsertions(self, s: str) -> int:
        i   = 0
        cpt = 0
        ins = 0
        while i < len(s):
            if s[i] == '(':
                cpt += 1
                i   += 1
                continue
            if cpt > 0:
                cpt -= 1
            else:
                ins += 1
            if i < len(s) - 1 and s[i + 1] == ')':
                i += 2
            else:
                i   += 1
                ins += 1
        return ins + cpt * 2