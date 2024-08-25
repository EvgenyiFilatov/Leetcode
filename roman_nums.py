class Solution:
    def romanToInt(self, s: str) -> int:
        rom_nums = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summa = 0
        for i in range(len(list(s))):
            if i == len(list(s)) - 1:
                summa += rom_nums[s[i]]
            elif rom_nums[s[i]] < rom_nums[s[i+1]]:
                summa -= rom_nums[s[i]]
            else:
                summa += rom_nums[s[i]]
        return summa


summa = Solution()
s = "MCMXCIV"
print(summa.romanToInt(s))
