# ORIGINAL SOLUTION - REMOVES ZEROS EVEN IF ALREADY AT THE END

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

# OPTIMIZED

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        
        
        
