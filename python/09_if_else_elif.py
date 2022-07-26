age = input("What is your age  9")
required_age = 5
age = int(age)
# Hammad can go to school?

if age==required_age:
    print("Congratulations! hammad can join the school.")
elif age > required_age:
    print("You Should have to Join a secondary School")    
elif age <= 2:
    print("You should take care of your baby.")    
else:
    print("You can not go to School")