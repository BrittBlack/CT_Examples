#Exercise 5: Fitness Advice
#
#
#
#
minutes_exercised_daily = float(input("How may minutes do you exercise daily?"))


if 0 <= minutes_exercised_daily <= 10 :
    print("Get up and move more! You need at least 30 minutes of exercise daily.")
elif 11 <= minutes_exercised_daily <= 19 :
    print("Great job! You have almost reached your goal of 30 minutes of exercise daily.")
elif 20 <= minutes_exercised_daily <= 29 :
    print("You are so close to your goal of exercising 30 minutes daily")
elif minutes_exercised_daily == 30 :
    print("You've reached your goal of exercising 30 minutes daily")
else:
    print("You've exceeded your exercise goal of 30 minutes daily. Consult your doctor!")
