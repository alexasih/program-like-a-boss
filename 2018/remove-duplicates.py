class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        else:
            start = nums[0]
            for num in nums[1:]:
                if num == start:
                    nums.remove(num)
                start = num
        return len(nums)
        
