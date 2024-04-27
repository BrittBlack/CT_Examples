#Exercise4 : Grading System
#
#
#
your_grade = 60
A = range(90,100)
B = range(80,89)
C = range(70,79)
D = range(60,69)
F = range(0,59)

if 90 <= your_grade <=100:
    print("Perfect!")

elif 80 <= your_grade <=89:
    print("Good Job!")

elif 70 <= your_grade <=79:
    print("Okay!")

elif 60 <= your_grade <=69:
    print("Almost!")

elif 0 <= your_grade <=59:
    print("Fail!")

else:
    print("How!")
