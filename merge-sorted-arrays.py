def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    i=j=0
    ret = []
    
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] < alices_list[j]:
            ret.append(my_list[i])
            i+=1
        else:
            ret.append(alices_list[j])
            j+=1
    
    while i < len(my_list):
        ret.append(my_list[i])
        i+=1
    
    while j < len(alices_list):
        ret.append(alices_list[j])
        j+=1


    return ret
