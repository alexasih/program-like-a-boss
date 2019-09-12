def highest_product_of_3(list_of_ints):
    
    if len(list_of_ints) < 3:
        raise(Exception)
        
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest = max(list_of_ints[0],list_of_ints[1])
    lowest = min(list_of_ints[0],list_of_ints[1])
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for current in list_of_ints[2:]:
        # ordered this way so it is not checking current against current for any of the max or min
        highest_product_of_3 = max(highest_product_of_3, current*highest_product_of_2, current*lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2, current*highest, current*lowest)
        lowest_product_of_2 = min(lowest_product_of_2, current*highest, current*lowest)
        highest = max(current, highest)
        lowest = min(current, lowest)
    
    return highest_product_of_3
