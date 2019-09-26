class Solution:
    def removeVowels(self, S: str) -> str:
        for letter in S:
            if letter in 'aeiou':
                S = S.replace(letter, '')
        
        return S
        
