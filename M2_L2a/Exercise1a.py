#Exercise 1: Movie Night Decision

mood = input("How are you feeling today? (happy/sad/adventurous): ")
weather = input("What's the weather like today? (sunny/rainy): ")



if mood == "happy":
    if weather == "sunny":
         print("Comedy")
    else:
        print("Adventure")
elif mood == "sad":
    print("Drama")
else:
    print("Adventure")

#
#
#
#Task 1 
#
#

temperature = int(input("What is today's temperature in Celsius? "))

event = input("What type of event are you attending? (formal/casual):")

if 0 <= temperature <= 9:
    if event == "formal":
        print("Wear your suit and parka.")
    else:
        print("Just dress warmly.")
elif 10 <= temperature <= 20 :
    print("Wear your suit and a light jacket.")
elif 21 >= temperature :
    print("Wear a blouse and slacks without a jacket.")
else: 
    print("Dress comfortable and causual. Be you.")

