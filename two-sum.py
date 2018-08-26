class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nextnum = nums[1:]
        for num in range(len(nums)):
            for nxt in range(len(nextnum)):
                summ=nums[num]+nextnum[nxt]
                if ((summ == target) and (num != nxt+1)):
                    return [num, nxt+1]
                
        return None
