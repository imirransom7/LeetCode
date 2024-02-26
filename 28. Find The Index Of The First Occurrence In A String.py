class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      
      return haystack.find(needle)
      
      # OR

      # loop using range to get the indices of the string
      for i in range(len(haystack)):
                  # check if it any index bewtween i and the length of the needle in a sub string; it will
                  # check if the word a substring inside of the haystack
                  if haystack[i : i+len(needle)] == needle:
                      return i
                  else:
                      return -1
