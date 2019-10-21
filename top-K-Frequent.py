# nlogn time

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = {}
        for word in words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        
        ret = sorted(d, key=lambda word: (-d[word], word))
        
        return ret[:k]
