class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # removing any whitespace in the beginnig and end of the string
        s = s.strip()
        # converting string into a list with spaces as the delimeter
        s = s.split(' ')
        # saving the last of the index of new list to a new variable since the last index will be the last word
        last_word = s[-1]
        return len(last_word)
