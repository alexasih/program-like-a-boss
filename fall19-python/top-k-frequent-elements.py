class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        count=0
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)}
        

        for num in sorted_freq:
            ret.append(num)
                
            if len(ret) == k:
                return ret
        
