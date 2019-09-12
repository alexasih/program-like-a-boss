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
    
def merge_ranges(meetings):
   
    merge(meetings)
    
    # merge list
    ret = [meetings[0]]
    meetings = meetings[1:]

    for meeting in meetings:
        last = ret[-1]
        
        if meeting[0] <= last[1]:
            
            ret[-1] = (last[0], max(last[1],meeting[1]))
        
        else:
            
            ret.append((meeting[0],meeting[1]))
            
    return ret
