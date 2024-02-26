class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_list = []
        for digit in digits:
            new_list.append(str(digit))
        s = "".join(new_list)
        s = int(s) + 1
        s = str(s)

        new_digits = []
        for i in s:
            new_digits.append(int(i))
        return new_digits
