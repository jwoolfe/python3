age = input("What is your age?: ")

def checkDriverAge(age=1):
    if int(age) < 18:
	    print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
	    print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
	    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(age)