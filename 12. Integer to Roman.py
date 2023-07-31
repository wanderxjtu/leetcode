class Solution:
    def intToRoman(self, num: int) -> str:
        i2r_map={ 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M", }

        rs = ""
        for n in sorted(i2r_map.keys(), reverse=True):
            cnt = floor(num / n)
            r = i2r_map[n]
            rs = rs + r*cnt
            num = num % n
        return rs
