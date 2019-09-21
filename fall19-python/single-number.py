class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        
        doubles = {}
        for num in nums:
            if num not in doubles:
                doubles[num] = 1
            else:
                doubles[num] += 1
        
        for num in doubles:
            if doubles[num] == 1:
                return num
