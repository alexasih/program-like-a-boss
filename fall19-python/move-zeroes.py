class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # if the zeros are before the next available integer, then swap
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        
        while count > 0:
            nums.remove(0)
            nums.append(0)
            count -= 1
