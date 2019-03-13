import datetime
def calculate_age():
    now = datetime.datetime.now()
    year = int(input("which year were you born? "))
    if year > 2019:
        print("Invalid input")
    elif year < 2019:
        age = now.year - year

        print("Your age is " + str(age))
    
        if age < 18:
            print("you are a minor")

        elif age < 36:
            print("you are a youth")

        elif age >= 36:
            print("you are an elder")

calculate_age()