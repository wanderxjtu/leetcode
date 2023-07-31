class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distances = dict()
        indices = dict()
        for idx, n in enumerate(nums):
            if n in indices:
                dist = idx - indices[n]
                if dist <= k:
                    return True
            indices[n] = idx # update last number index
        return False

