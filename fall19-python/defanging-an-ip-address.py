class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = address
        for char in address:
            if char == '.':
                new=address.replace(char, '[.]')
        
        return new
        
