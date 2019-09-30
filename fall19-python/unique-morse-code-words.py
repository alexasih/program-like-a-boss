class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        alphabet = {}
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(morse)):
            if letters[i] not in alphabet:
                alphabet[letters[i]] = morse[i]
        
        morse_words = []
        for word in words:
            new = ''
            for letter in word:
                new += alphabet[letter]
            morse_words.append(new)
        
        return len(set(morse_words))
                
                
        
        
        
        
