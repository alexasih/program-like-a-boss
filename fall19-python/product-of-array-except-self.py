# slow solution O(n^2)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = []
        
        for i in range(len(nums)):
            thisSum=1
            for j in range(len(nums)):
                if i!=j:
                    thisSum*=nums[j]
            ret.append(thisSum)
        return ret
                    
