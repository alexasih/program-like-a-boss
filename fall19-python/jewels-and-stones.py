# TIME OPTIMIZED

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count = 0
        stone_dict = {}
        for stone in S:
            if stone not in stone_dict:
                stone_dict[stone] = 1
            else:
                stone_dict[stone] += 1
        
        for jewel in J:
            if jewel in stone_dict:
                count += stone_dict[jewel]
        
        return count

# ANOTHER SLOW/BRUTE FORCE SOLUTION

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count = 0
        
        for s in S:
            for j in J:
                if s==j:
                    count+=1
        return count
        
# SLOW SOLUTION

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count=0
        for stone in S:
            if stone in J:
                count+=1
        return count
        
