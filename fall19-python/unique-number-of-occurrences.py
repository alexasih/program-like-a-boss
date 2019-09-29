class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        repeat_dict = {}
        comparisons = []
        
        if arr == [] or len(arr) == 1:
            return True
        
        for val in arr:
            if val not in repeat_dict:
                repeat_dict[val] = 1
            else:
                repeat_dict[val] += 1
        
        for val in repeat_dict:
            comparisons.append(repeat_dict[val])
        
        is_unique = set(comparisons)
        
        if len(is_unique) != len(comparisons):
            return False
            
        return True
