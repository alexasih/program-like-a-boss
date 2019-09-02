def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    
    string_dict = {}
    
    # think about edge cases - like empty or one letter strings
    if len(the_string) < 2:
        return True
        
    for letter in the_string:

        if letter not in string_dict:
            string_dict[letter] = 1
        else:
            if string_dict[letter] == 2:
                return False
            string_dict[letter] += 1
    
    if ((len(the_string) % 2 == 0) and (len(string_dict) == len(the_string)//2)) or ((len(the_string) % 2 == 1) and (len(string_dict) == len(the_string)//2+1)):
        return True
        
    return False
