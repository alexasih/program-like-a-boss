def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time - using counting sort
    ret = []
    temp = 0
    # indexes start at 0, so need to add 1 to include highest score
    scores = [0] * (highest_possible_score+1)
    
    # add counts to scores list for each score that appears in unsorted_scores
    for score in unsorted_scores:
        scores[score] += 1
    
    # for each score in the range until reaching -1, decrement by 1
    # count is the number of times a score appears
    for score in range(len(scores)-1,-1,-1):
        count = scores[score]
    
        # then append the score to the list the number of times it appears
        for time in range(count):
            
            ret.append(score)

    return ret
