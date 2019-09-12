class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        self.words_to_counts = {}
        self.add_to_dict(input_string)
    
    def add_to_dict(self, input_string):
        # make sure all punctuation is removed
        for val in input_string:
            if val in ":,!?;.":
                input_string = input_string.replace(val," ")
        
        if " - " in input_string:
            input_string = input_string.replace(" - "," ")
            
        input_string = input_string.split()
        
        for word in input_string:
            
            if word not in self.words_to_counts and word.capitalize() not in self.words_to_counts:
                self.words_to_counts[word] = 1
            elif word in self.words_to_counts:
                self.words_to_counts[word] += 1
            # if the word is ever all lowercase, remove capitalized because it was only capitalized because 
            # it was at the beginning of a sentence
            elif word.capitalize() in self.words_to_counts and word != word.capitalize():
                self.words_to_counts.pop(word.capitalize())
                self.words_to_counts[word] = 2
