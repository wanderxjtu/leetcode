class Solution:
    def longestPalindrome(self, s: str) -> str:
         # found 3 letter-palindromic indices
        p3indices = []
        p2indices = []
        for i in range(len(s)-2):
            if s[i]==s[i+2]:
                p3indices.append(i+1)  # center of p3
            if s[i]==s[i+1]:
                p2indices.append(i) # left center of p2
        if s[-1] == s[-2]:
            p2indices.append(len(s)-1)
        print(p3indices, p2indices)

        maxstart=0
        maxp=1
        for p3 in p3indices:
            for i in range(1, int(len(s)/2)+1):
                print(p3, i)
                if p3-i < 0 or p3+i >= len(s):
                    break
                if s[p3-i] != s[p3+i]:
                    break
                if 2*i+1 > maxp:
                    maxp=2*i+1
                    maxstart = p3-i

        for p2 in p2indices:
            for i in range(0, int(len(s)/2)+1):
                if p2-i < 0 or p2+1+i >= len(s):
                    break
                if s[p2-i] != s[p2+1+i]:
                    break
                if 2*i + 2 > maxp:
                    maxp=2*i+2
                    maxstart = p2-i
                    
        print(maxstart, maxp)
        return s[maxstart:maxstart+maxp]

print(Solution().longestPalindrome("babad"))
