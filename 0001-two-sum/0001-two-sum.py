class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Ayaaaa, sans test agents tu peux rien faire?
        On en talk ?
        Allez tu fais quoi ?
        Ayaaa, toute de suite c'est un blanc ? ragix
        '''
        seen = {}
        for i, num in enumerate(nums):
            r = target - num
            if r in seen:
                return [seen[r], i]
            seen[num] = i
        return []