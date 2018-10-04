class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for elem in nums:
            if elem not in dict:
                dict[elem] = 1
            else:
                dict[elem] += 1
        max_count = 0
        max_elem = 0
        for key in dict: 
            if dict[key] > max_count:
                max_count = dict[key]
                max_elem = key
        return max_elem
        
