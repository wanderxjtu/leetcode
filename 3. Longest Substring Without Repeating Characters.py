class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        start = -1   # so 0-(-1) == 1
        maxlength = 0
        for idx, char in enumerate(s):
            if char in pos and start < pos[char]:  # start must increasing
                start = pos[char]
            if idx - start > maxlength:
                maxlength = idx - start
            pos[char] = idx
        return maxlength
