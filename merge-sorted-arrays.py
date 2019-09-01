def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    i=j=k=0
    ret = [None] * (len(my_list) + len(alices_list))
    
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] < alices_list[j]:
            ret[k] = my_list[i]
            i+=1
        else:
            ret[k]=alices_list[j]
            j+=1
        k+=1
    
    while i < len(my_list):
        ret[k] =my_list[i]
        i+=1
        k+=1
    
    while j < len(alices_list):
        ret[k] =alices_list[j]
        j+=1
        k+=1

    return ret
