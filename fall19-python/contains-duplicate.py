class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = {}
        
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        
        for val in dictionary:
            if dictionary[val] > 1:
                return True
        return False

# OPTIMIZED

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        original_length = len(nums)
        
        nums = set(nums)
        
        if original_length != len(nums):
            return True
        return False
        
# ANOTHER OPTIMIZED SOLN

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = {}
        
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                return True
        return False
            
        
        
        
