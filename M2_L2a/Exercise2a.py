#Exercise 2: Quick Temperature Check

temperature = int(input("What is today's temperature in Celsius? "))

event = input("What type of event is this? (formal/casual): ")

if 0 <= temperature <= 15:
    if event == "formal":
        print("Warm formal suit.")
    else:
        print("Wear a cozy sweater and jeans.")
elif 15 <= temperature <= 35:
    print("Light formal suit")
else:
    print("T-shirt and shorts.")