required_age_at_school = 5
student_age = input("Enter Your age? ")
student_age = int(student_age)
# quetsion: can students go to school

if student_age==required_age_at_school: #for checking equal or not
    print("Congratulations, you can join the school.")
elif student_age > required_age_at_school: #for checking age is greater than or not
    print("You should have to join a higer school")
elif student_age <=2 : #for checking age is less than or equal to than or not
    print("You, Should take care of your baby")
else:
    print("Sorry, you cannot got to school") # If nothing works
