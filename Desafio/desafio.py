import funciones

# Invoco la función para cargar las duraciones de peliculas.
movies = []
movies = funciones.input_movies()

# Invoco la función para calcular el promedio.
average = funciones.average_calculation(movies)

# Invoco la función para informar las peliculas que superan el promedio.
funciones.max_average(movies,average)
