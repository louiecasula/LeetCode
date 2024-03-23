class Solution:
    def intToRoman(self, num: int) -> str:
        # Map each symbol to it's value
        out = ""
        roman = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        # While number > 0, decrement by largest value in map, append key to output string
        while num > 0:
            for key in roman:
                if key <= num:
                    out += roman[key]
                    num -= key
                    break
        # Return output string
        return out