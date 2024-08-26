"""12. Integer to Roman,
https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    # метод "влоб"
    def intToRoman(self, num: int) -> str:
        rom_num: str = ''
        num_str = str(num)
        i: int = len(num_str) - 1
        k: int = 1
        while i >= 0:
            if k == 1:
                if num_str[i] == '9':
                    rom_num = 'IX' + rom_num
                elif num_str[i] == '4':
                    rom_num = 'IV' + rom_num
                elif num_str[i] < '4':
                    rom_num = 'I' * int(num_str[i]) + rom_num
                elif num_str[i] == '5':
                    rom_num = 'V' + rom_num
                else:
                    rom_num = 'V' + 'I' * (int(num_str[i]) - 5) + rom_num
            elif k == 2:
                if num_str[i] == '9':
                    rom_num = 'XC' + rom_num
                elif num_str[i] == '4':
                    rom_num = 'XL' + rom_num
                elif num_str[i] < '4':
                    rom_num = 'X' * int(num_str[i]) + rom_num
                elif num_str[i] == '5':
                    rom_num = 'L' + rom_num
                else:
                    rom_num = 'L' + 'X' * (int(num_str[i]) - 5) + rom_num
            elif k == 3:
                if num_str[i] == '9':
                    rom_num = 'CM' + rom_num
                elif num_str[i] == '4':
                    rom_num = 'CD' + rom_num
                elif num_str[i] < '4':
                    rom_num = 'C' * int(num_str[i]) + rom_num
                elif num_str[i] == '5':
                    rom_num = 'D' + rom_num
                else:
                    rom_num = 'D' + 'C' * (int(num_str[i]) - 5) + rom_num
            else:
                rom_num = 'M' * int(num_str[i]) + rom_num
            k += 1
            i -= 1
        return rom_num

    # второй варант, усовершенствованный
    def intToRoman2(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num


int_to_roman = Solution()
num = 3749
print(int_to_roman.intToRoman(num))
print(int_to_roman.intToRoman2(num))
