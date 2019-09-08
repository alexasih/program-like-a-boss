def find_repeat(numbers):

    # Find a number that appears more than once
    numbers = sorted(numbers)
    print(numbers)
    floor_index = 0
    ceiling_index = len(numbers)-1
    
    distance = ceiling_index - floor_index
    guess_index = distance // 2
    guess_value = numbers[guess_index]
    
    if numbers[floor_index] < numbers[ceiling_index]:
         floor_index = guess_index
        
    else:
        ceiling_index = guess_index
        
    if numbers[floor_index] == numbers[ceiling_index]:
        return numbers[floor_index]


    return "None"
