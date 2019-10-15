class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dictionary = {}
        
        for i in range(len(list1)):
            if list1[i] not in dictionary:
                dictionary[list1[i]] = [i]
        
        for i in range(len(list2)):
            if list2[i] in dictionary:
                dictionary[list2[i]].append(i)
        
        max_index = len(list1)+len(list2)
        value = ''
        for val in dictionary:
            print(val)
            if len(dictionary[val]) > 1:
                current_sum = 0
                for index in dictionary[val]:
                    current_sum+=index
                if current_sum < max_index:
                    max_index=current_sum
                    value = [val]
                elif current_sum == max_index:
                    value.append(val)
                    
        return value
                
