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
        # by each dictionary value in reverse (greatest value to least)
        # for each word in dictionary
        
        # first, sorts by values in dictionary
        # then sorts again by word, which alphabetizes
        ret = sorted(d, key=lambda word: (-d[word], word))

        return ret[:k]
