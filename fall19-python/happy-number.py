class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n == 0:
            return False
        
        tracker = {}
        
        while n > 1:
            
            if n in tracker:
                return False
            if n not in tracker:
                tracker[n] = 1
            
            n_sum = 0
            for val in str(n):
                n_sum += int(val) ** 2
            
            n = n_sum
        
        return True
