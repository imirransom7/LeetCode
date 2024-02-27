class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      # This soultion works but does not complete the time complexity; this is prabably a better solutuon for 'Most Occurring Number'
      # Setting counter
      counter = 0
      majority = 0

      for num in nums:
          # using count method to see if the number of appearences are bigger than our counter
          # if so, then that is the new majority number
          if nums.count(num) > counter:
              counter+=1
              majority = num
      # returning the majority number
      return majority



      # BETTER SOULTION FOR THIS PROBLEM
      # this beats the time complexity
      for num in nums:
        # checks to see if the count of the element is greater than half of the list; if it is then that is the majority number
        if nums.count(num) > len(nums)//2:
            # Returning the majority number
            return num
