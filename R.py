class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            if s[i] == 'I':
                counter += 1
            elif s[i] == 'V':
                if s[i-1] == 'I':
                    counter -= 1
                    counter += 4
                else:
                    counter += 5
            elif s[i] == 'X':
                if s[i-1] == 'I':
                    counter -= 1
                    counter += 9
                else:
                    counter += 10
            elif s[i] == 'L':
                if s[i-1] == 'X':
                    counter -= 10
                    counter += 40
                else:
                    counter += 50
            elif s[i] == 'C':
                if s[i-1] == 'X':
                    counter -= 10
                    counter += 90
                else:
                    counter += 100
            elif s[i] == 'D':
                if s[i-1] == 'C':
                    counter -= 100
                    counter += 400
                else:
                    counter += 500
            elif s[i] == 'M':
                if s[i-1] == 'C':
                    counter -= 100
                    counter += 900
                else:
                    counter += 1000

        return counter
            





class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for i in s:
            counter += roman[i]

        return counter
            
        
