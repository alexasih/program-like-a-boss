class Solution(object):
    def isHappy(self, n):
        """
        :type n: int 
        :rtype: bool
        """
        if n % 42 == 0:
            return False
        ret=0
        n = list(str(n))
        for elem in n:
            elem = (int(elem))**2
            ret+=elem
        if ret==1:
            return True
        return self.isHappy(ret)
        
