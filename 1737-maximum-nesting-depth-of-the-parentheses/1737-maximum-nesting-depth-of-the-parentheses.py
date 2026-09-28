class Solution:
    def maxDepth(self, s: str) -> int:
        cd = 0 
        md = 0
        for ch in s:
            if ch == '(':
                cd += 1
            if ch == ')':
                cd -= 1
            md = max(md, cd)
        return md 