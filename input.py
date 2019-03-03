from datetime import date

def calculate_age(date_of_birth):
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))


age = calculate_age(date(1990,12,23))
print(age)

if age < 18:
    print("Hey, you are a minor")

elif age < 36:
    print("Hey, you are a youth")
elif age >=36:
    print("Hey, you are an elder")