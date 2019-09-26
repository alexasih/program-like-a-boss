class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        nums = sorted(nums)
        repeat = {}
        ret = []
        
        for num in nums:
            if num not in repeat:
                repeat[num] = 1
            else:
                repeat[num] += 1
        
        for num in repeat:
            if repeat[num] > 1:
                ret.append(num)
        
        return ret
                
        
