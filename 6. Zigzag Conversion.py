class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # group = 2*numRows - 2
        # first line would be group's first letters
        #

        # groupby
        if numRows == 1:
            return s
        strings = numRows*[""]
        elecnt = 2*numRows-2
        for i, c in enumerate(s):
            pos = i % elecnt
            if pos < numRows:
                strings[pos] += c
            else:
                strings[elecnt - pos] +=c
        return "".join(strings)


