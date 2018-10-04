class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ret = []
        dict = {}
        A = A.split(" ")
        B = B.split(" ")
        for word in A:
            if word not in dict:
                dict[word] = 1
            else: 
                dict[word] += 1
        for word in B:
            if word not in dict:
                dict[word] = 1
            else: 
                dict[word] += 1
        for elem in dict:
            if dict[elem] == 1:
                ret.append(elem)
        return ret
                
