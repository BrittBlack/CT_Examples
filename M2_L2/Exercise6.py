#Exercise 6 : Coffee Recommendation
#
#
#
#
likes_sweet = input("Do you like your coffee sweet? (yes/no) ")
likes_milk = input("Do you like your coffee sweet? (yes/no) ")

if likes_sweet == "yes" and likes_milk == "yes":
    print("How about a caramel latte?")
if likes_sweet == "no" and likes_milk == "yes":
    print("An americano with a dash of milk sounds good for you.")
if likes_sweet == "yes" and likes_milk == "no":
    print("Try a black coffee with two sugar cubes.")
else:
    print("Black coffee it is!")