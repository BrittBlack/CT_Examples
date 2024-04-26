#Exercise 2: Movie Age Restriction
#
#
#
movie_rating = "X"
age = 100

if movie_rating == "G" and age != 0:
    print("Based on your age, you may watch this movie.")
elif movie_rating == "PG" and age < 13:
    print("Based on your age, you may watch this movie with a parent.")
elif movie_rating == "PG-13" and age == 13:
    print("Based on your age, you may watch this movie with a parent.")
elif movie_rating == "R" and age >= 17:
    print("Based on your age, you may watch this movie.")
else:
    print("You should not be watching this.")