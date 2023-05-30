class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n not in count.keys():
                count[n] = 1
            else:
                return True
        return False
