# nlogn time

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = {}
        for word in words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        
        # sort the dictionary d by the dictionary value
        # using lambda for the key value, so that it sorts
        # by each dictionary value in reverse (greatest to least)
        # for each word in dictionary
        ret = sorted(d, key=lambda word: (-d[word],word))
        # why can't we do just (-d[word])?
        
        return ret[:k]
