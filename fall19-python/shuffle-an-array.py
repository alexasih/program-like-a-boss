import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        
        ret = self.original
        ret = sorted(ret)
        return ret
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ret = self.original
        print(ret)
        for i in range(len(ret)):
            rand = random.randint(i, len(ret)-1)
            print(rand)
            temp = ret[i]
            ret[i] = ret[rand]
            ret[rand] = temp
        return ret
    
