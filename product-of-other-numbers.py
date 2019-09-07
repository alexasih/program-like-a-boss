def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list) < 2:
        raise(Exception)
    elif len(int_list) == 2:
        temp = int_list[0]
        int_list[0] = int_list[1]
        int_list[1] = temp
        return int_list
    
    before_product = 1
    after_product = 1
    
    ret = [None] * len(int_list)
    
    for i in range(len(int_list)):
        ret[i] = before_product
        before_product *= int_list[i]
    
    for i in range(len(int_list)-1,-1,-1):
        ret[i] *= after_product
        after_product *= int_list[i]
    
    return ret
