def merge(meetings):
    
    # Sort input list by start time
    if len(meetings) > 1:
        mid = len(meetings) // 2
        l = meetings[:mid]
        r = meetings[mid:]
        
        merge(l)
        merge(r)
        
        i = j = k = 0
        
        while i < len(l) and j < len(r):
            if l[i][0] < r[j][0]:
                meetings[k] = l[i]
                i += 1
            else:
                meetings[k] = r[j]
                j += 1
            k+=1
        
        while i < len(l):
            meetings[k] = l[i]
            i+=1
            k+=1
        
        while j < len(r):
            meetings[k] = r[j]
            j+=1
            k+=1
