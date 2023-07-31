class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for n in nums:
            if n in numset:
                return True
            numset.add(n)
        return False

