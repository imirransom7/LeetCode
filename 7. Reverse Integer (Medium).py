class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        # getting the maximum and minimum range for a signed 32-bit integer range
        num_max = 2**31
        num_min = -2**31
        

        # taking the the negative symbol out
        # since the string is reversed, the symbol will always be the last index in the string
        if s[-1] == '-':
            s = s[:-1]
            s = int(s)
            # changing the number back into a negative
            s = s * (-1)
    
        if int(s) > num_max or int(s) < num_min:
            return 0
        else:
            return int(s)
