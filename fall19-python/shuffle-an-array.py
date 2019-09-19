import random 

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.shuffled=nums
        self.original=nums[:]
       
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.shuffled)):

            rand=random.randint(i,len(self.shuffled)-1)
            
            self.shuffled[i],self.shuffled[rand] = self.shuffled[rand],self.shuffled[i]
            
        return self.shuffled
