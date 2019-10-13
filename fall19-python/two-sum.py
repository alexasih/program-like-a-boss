# optimized

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if nums == [] or len(nums) == 1:
            return []
        
        dictionary = {}
        
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[target-nums[i]] = i
            else: 
                return [dictionary[nums[i]], i]
                

# solution so slow time limit exceeded lol

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if nums == [] or len(nums) == 1:
            return []
        
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i!=j and nums[i]+nums[j] == target:
                    return [i,j]
        return []
        
