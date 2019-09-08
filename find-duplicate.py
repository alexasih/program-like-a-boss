# First solution with O(n) for space
def find_repeat(numbers):

    number_dict = {}
    for n in numbers:
        if n not in number_dict:
            number_dict[n] = 1
        else:
            number_dict[n] += 1
    
    for n in number_dict:
        if number_dict[n] > 1:
            return n
    return "None"

# Second solution
def find_repeat(numbers):

    # Find a number that appears more than once
    
    numbers = sorted(numbers)
    
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            return numbers[i]
    return "None"

# third solution - best O(1) space, O(nlgn) time
  def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:

        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        items_in_lower_range = 0
        for item in numbers:
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
          
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
        
            floor, ceiling = upper_range_floor, upper_range_ceiling

    return floor
