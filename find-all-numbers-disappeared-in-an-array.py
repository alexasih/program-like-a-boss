class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # use hash table for faster lookups otherwise 
        hashing = {}
        
        if len(nums) < 2:
            return []
        
        ret = []
        for val in nums:
            hashing[val] = 1
        
        for i in range(1,len(nums)+1):
            if i not in hashing:
                ret.append(i)
                    
        return ret
        
