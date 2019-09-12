class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index=-1
        if len(digits)==1 and digits[0] != 9:
            digits[0]=digits[0]+1
            return digits
        while digits[index]==9:
            digits[index]=0
            if abs(index)==len(digits):
                break
            index=index-1
        if len(digits)==abs(index) and digits[0]==0:
            digits.insert(0, 1)
            return digits
        digits[index]=digits[index]+1
        return digits
