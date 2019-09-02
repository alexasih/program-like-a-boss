def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    i=j=k=0
    
    if len(take_out_orders) == 0 or len(dine_in_orders) == 0:
        
        # assuming that if there is only one type of order, 
        # then the ordering problem will not occur

        return True
    
    if len(served_orders) != (len(take_out_orders)+len(dine_in_orders)):
        
        # don't forget to account for FORGOTTEN orders!!!
        
        return False
            
            
    while (i < len(take_out_orders) and k < len(served_orders)) and (j<len(dine_in_orders) and k < len(served_orders)):
        
        if served_orders[k] == take_out_orders[i]:
            i+=1
            k+=1
        elif served_orders[k] == dine_in_orders[j]:
            j+=1
            k+=1
        else:
            return False
        
    while i < len(take_out_orders) and k < len(served_orders):

        if served_orders[k] != take_out_orders[i]:
            print("this is k",k)
            print("this is i",i)
            return False
        i+=1
        k+=1
        
    
    while i<len(dine_in_orders) and k < len(served_orders):
        if served_orders[k] != dine_in_orders[j]:
            print("this is k",k)
            print("this is j",j)
            return False
        j+=1
        k+=1 
    
    return True
