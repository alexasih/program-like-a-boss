class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if int(x) < 0:
            return False
        elif len(x) == 1:
            return True
        length = int(len(x)/2)
        x1 = x[:length]
        x2 = x[-length:]
        val=0
        for elem in x2[::-1]:
            if elem != x1[val]:
                return False
            val=val+1
        return True
