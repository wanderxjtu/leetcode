class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        ret = []
        for n in nums:
            nn = nums.copy()
            nn.remove(n)
            print(nn)
            for e in self.permute(nn):
                print(nn, e, n)
                ret.append([n] + e)
        return ret


print(Solution().permute([1,2,3]))
