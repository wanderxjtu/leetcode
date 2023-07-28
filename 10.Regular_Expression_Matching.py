class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        patterns=self._parse(p)
        
        return self._match(s, patterns)

    def _parse(self, p: str) -> list:
        start = 0
        ret = []
        for idx, c in enumerate(p):
            if c == '*':
                if idx - 1 > start:  # not start just before *
                    ret.append(p[start:idx - 1])  # previous str
                if len(ret)==0 or ret[-1] not in ('.*', p[idx-1:idx+1]): #merge any pattern
                    ret.append(p[idx -1:idx +1])  # * str
                start = idx + 1 # update start idx to 
            elif idx == len(p)-1:  # last char but not *
                ret.append(p[start:])
        # TODO: merge same pattern
        return ret

    def _match(self, s, patterns):
        print(s, patterns)
        if len(patterns) == 0 and len(s) == 0:
            return True
        if len(s) > 0 and len(patterns) == 0:
            return False
        for p in patterns:
            if p[-1] != "*":
                # must match
                if len(s) < len(p): # no enough str to match
                    return False
                for c, pc in zip(s, p):
                    if pc != '.' and c != pc:
                        return False
                return self._match(s[len(p):], patterns[1:])
            else:
                if len(s) == 0:
                    return self._match(s, patterns[1:])
                # allow zero
                if s[0] != p[0] and p[0] != '.':
                    return self._match(s, patterns[1:])  # try next pattern
                if self._match(s[1:], patterns): # >= 1 char, take this pattern
                    return True
                return self._match(s, patterns[1:])  # drop this pattern
        return True
                



print(Solution().isMatch("mississippi", "mis*is*p*."))
print(Solution().isMatch("aab", "c*a*b"))
print(Solution().isMatch("aab", "c*.*b"))
print(Solution().isMatch("aa", "a*"))
print(Solution().isMatch("aa", ".*c"))
print(Solution().isMatch("bab", "..*"))
print(Solution().isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"))


