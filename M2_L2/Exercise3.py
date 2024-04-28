#Exercise 3: Weather Suggestion
#
#
#
current_temperature = float(input("Enter today's temperature in Fahrenheit: "))

if  0 <= current_temperature <= 24:
    print("Put on your apple bottom jeans, boots with the fur, and maybe stay inside")
elif 25 <= current_temperature <= 49:
    print("You can get away with shorts, a sweater, and a parka.")
elif 50 <= current_temperature <= 75:
    print("Enjoy the weather, wear whatever you like")
elif 76 <= current_temperature <= 100:
    print("Just wear a swim suit out.")
else:
    print("Don't put on clothes, stay inside.")