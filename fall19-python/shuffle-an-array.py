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

    
#     already_visited_indices = set()
#     unvisited_indices = set()
#     ret = [None] * len(x)
    
#     for i in (range(len(x)//2):
#         curr_rand = Random(0,len(x))
#         if curr_rand not in already_visited_indices:
#             ret[i] = x[curr_rand]
#             already_visited_indices.append(curr_rand)
        
    
#     for i in (range(len(x)):
#         if x[i] not in already_visited_indices:
#               unvisited_indices.append(i)
    
#     for 
        
    
#     return ret
