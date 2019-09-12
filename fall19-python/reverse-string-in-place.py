def reverse(list_of_chars):

    # Reverse the input list of chars in place
    temp = ''
    val=0
    rev=-1
    while val < len(list_of_chars)//2:
        
        temp = list_of_chars[val]
        list_of_chars[val] = list_of_chars[rev]
        list_of_chars[rev] = temp
        
        val+=1
        rev-=1
        
    pass
