def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # Shuffle the input in place
    
    if len(the_list) <= 1:
        return the_list
    for i in range(len(the_list)):
        temp = the_list[i]
        random_val = get_random(0,len(the_list)-1)
        if i != random_val:
            the_list[i] = the_list[random_val]
            the_list[random_val] = temp
    pass
