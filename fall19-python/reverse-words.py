def reverse_characters(message, left_index, right_index):
    
    temp = ''

    while left_index < right_index:
        temp = message[left_index]
        message[left_index] = message[right_index]
        message[right_index] = temp
        left_index +=1
        right_index -=1

def reverse_words(message):
    
    # Decode the message by reversing the words
    
    reverse_characters(message, 0, len(message)-1)

    left_index = 0
    
    for i in range(len(message)):
        
        if (i==len(message)-1):
            reverse_characters(message, left_index, i)
        elif (message[i] == ' '):
            reverse_characters(message, left_index, i-1)
            left_index = i+1
