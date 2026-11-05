class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        dval = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                dval += 1
        return dval