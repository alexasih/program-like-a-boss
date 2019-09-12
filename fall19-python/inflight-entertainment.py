def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    
    # Think about movies being the same length - MUST be accounted for!

    movie_dict = {}

    for movie in movie_lengths:
        if movie not in movie_dict:
            movie_dict[movie] = 1
        else:
            movie_dict[movie] += 1
    
    for movie in movie_lengths:
        second = flight_length - movie
        if movie == second: 
            if movie_dict[second] > 1:
                return True
        elif second in movie_lengths:
            return True
        

    return False
