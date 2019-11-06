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

# another nlogn solution

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        ret=[]
        freq = {}
        for word in words:
            if word not in freq:
                freq[word]=1
            else:
                freq[word]+=1
        
        sorted_freq = {key: value for key, value in sorted(freq.items(), key=lambda x: [-x[1], x[0]])}
        
        for word in sorted_freq:
            ret.append(word)
            
            if len(ret)==k:
                return ret
        
