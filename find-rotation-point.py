def find_rotation_point(words):

    if len(words) < 2:
        raise(Exception)
    # Find the rotation point in the list using binary search
    floor_index = -1
    ceiling_index = len(words)
    
    while floor_index + 1 < ceiling_index:
        
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        
        guess_value = words[guess_index]

        if guess_value == target:
            return guess_index

        if guess_value > target:
            # Target is to the left, so move ceiling to the left
            ceiling_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index

    return -1
