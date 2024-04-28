#Exercise 2: Movie Age Restriction
#
#
#
movie_rating = input("Enter movie rating (G, PG, PG-13,R): ")
age = int(input("Enter your age: "))

if movie_rating == "G" and age != 0:
    print("Based on your age, you may watch this movie.")
elif movie_rating == "PG" and age < 13:
    print("Based on your age, you may watch this movie with a parent.")
elif movie_rating == "PG-13" and age >= 13:
    print("Based on your age, you may watch this movie with a parent.")
elif movie_rating == "R" and age >= 17:
    print("Based on your age, you may watch this movie.")
else:
    print("You are not allowed to watch this movie.")