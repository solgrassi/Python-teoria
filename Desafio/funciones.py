def input_movies():
    """ 
    This function returns a list with the duration in minutes of the movies
    """
    minutes = int(input(
        "Ingresá la duración de una película  (0 para finalizar): "
    ))
    movies_duration  = []
    while minutes != 0:
        movies_duration .append(minutes)
        minutes = int(input(
            "Ingresá la duración de una película  (0 para finalizar)"
        ))
    return movies_duration


def average_calculation(movies_duration):
    """ 
    This function calculates the average of the lengths of the movies received 
    by movies_duration: is a list with the duration in minutes of the movies    
    """

    len_movies = len(movies_duration)
    average = float(0 if len_movies == 0 else sum(movies_duration) / len_movies)   
    return average


def max_average (movies_duration,average):
    """ 
    This function calculates the number of movies that last more than the 
    average duration
    """
    maax = [n for n in movies_duration if n > average]
    print(f"{len(maax)} películas duran más que el promedio ({average} min).")

