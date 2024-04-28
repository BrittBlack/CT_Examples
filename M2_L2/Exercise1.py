#Exercise 1: Traffic Light Simulator
#
#
traffic_light = input("Enter the traffic light color(red, yellow, green):")
#Using the input function allows you to give the user directions
if traffic_light == "red":
    print("Stop!")
elif traffic_light == "yellow":
    print("Caution!")
elif traffic_light == "green":
    print("Go!")
else:
    print("Please enter red, yellow, or green.")
    