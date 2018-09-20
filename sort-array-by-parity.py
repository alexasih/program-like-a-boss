class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_odd = []
        for val in A:
            if val % 2 == 0:
                even_odd.append(val)
        for val in A:
            if val % 2 == 1:
                even_odd.append(val)
        return even_odd
        
