def find_rotation_point(words):

    if len(words) < 2:
        raise(Exception)
    # Find the rotation point in the list using binary search
    first_word = words[0]
    floor_index = -1
    ceiling_index = len(words)
    
    while floor_index + 1 < ceiling_index:
        
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        
        guess_value = words[guess_index]

        if guess_value < first_word:
            ceiling_index = guess_index
        
        else:
            floor_index = guess_index
        
        if floor_index + 1 == ceiling_index:
            return ceiling_index

    return -1
