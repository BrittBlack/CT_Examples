#Exercise4 : Grading System
#
#
#
your_grade = float(input("Enter your grade (0 - 100): "))

if  your_grade >= 90:
    print("Your letter grade is A.")
elif your_grade >= 80:
    print("Your letter grade is B.")
elif your_grade >= 70:
    print("Your letter grade is C.")
elif your_grade >= 60:
    print("Your letter grade is D.")
else:
    print("Your letter grade is F.")
