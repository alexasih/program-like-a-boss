class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        for num in reversed(nums):
            if num == val:
                nums.remove(num)
        return len(nums)
