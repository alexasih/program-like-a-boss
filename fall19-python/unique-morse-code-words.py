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
                
                
# IMPROVED

# it is better to create the dictionary by hand, because otherwise every time this function is run, a new dictionary, alphabet, would be created unnecessarily when the values within the dictionary will never change
        
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        
        alphabet = {'a': ".-",
                    'b': "-...",
                    'c': "-.-.",
                    'd':"-..",
                    'e':".",
                    'f':"..-.",
                    'g':"--.",
                    'h':"....",
                    'i':"..",
                    'j':".---",
                    'k':"-.-",
                    'l':".-..",
                    'm':"--",
                    'n':"-.",
                    'o':"---",
                    'p':".--.",
                    'q':"--.-",
                    'r':".-.",
                    's':"...",
                    't':"-",
                    'u':"..-",
                    'v':"...-",
                    'w':".--",
                    'x':"-..-",
                    'y':"-.--",
                    'z':"--.."}
        
        # Sets are significantly faster when it comes to determining if an object is present in the set (as in x in s), but are slower than lists when it comes to iterating over their contents, so we use an array first then get the length of the set of that array
        morse_words = []
        for word in words:
            new = ''
            for letter in word:
                new += alphabet[letter]
            morse_words.append(new)
        
        return len(set(morse_words))
                
                
        
        
        
        

        
        
