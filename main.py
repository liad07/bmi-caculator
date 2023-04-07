gender = input("Enter your gender (M or F): ")
age = int(input("Enter your age in years: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if age < 2:
    print("BMI guidelines for infants and toddlers do not apply.")
elif age >= 2 and age < 5:
    if bmi < 13:
        print("Your BMI is considered underweight for your age.")
    elif bmi >= 13 and bmi <= 18.4:
        print("Your BMI is considered normal weight for your age.")
    elif bmi >= 18.5 and bmi <= 21.9:
        print("Your BMI is considered overweight for your age.")
    else:
        print("Your BMI is considered obese for your age.")
elif age >= 5 and age < 18:
    if bmi < 15:
        print("Your BMI is considered underweight for your age.")
    elif bmi >= 15 and bmi <= 20.9:
        print("Your BMI is considered normal weight for your age.")
    elif bmi >= 21.0 and bmi <= 24.9:
        print("Your BMI is considered overweight for your age.")
    else:
        print("Your BMI is considered obese for your age.")
elif age >= 18 and age <= 64:
    if gender == 'M':
        if bmi < 18.5:
            print("Your BMI is considered underweight.")
        elif bmi >= 18.5 and bmi <= 24.9:
            print("Your BMI is considered normal weight.")
        elif bmi >= 25.0 and bmi <= 29.9:
            print("Your BMI is considered overweight.")
        else:
            print("Your BMI is considered obese.")
    elif gender == 'F':
        if bmi < 18.5:
            print("Your BMI is considered underweight.")
        elif bmi >= 18.5 and bmi <= 24.9:
            print("Your BMI is considered normal weight.")
        elif bmi >= 25.0 and bmi <= 29.9:
            print("Your BMI is considered overweight.")
        else:
            print("Your BMI is considered obese.")
elif age >= 65:
    if gender == 'M':
        if bmi < 23.0:
            print("Your BMI is considered underweight.")
        elif bmi >= 23.0 and bmi <= 27.0:
            print("Your BMI is considered normal weight.")
        elif bmi >= 27.1 and bmi <= 30.0:
            print("Your BMI is considered overweight.")
        else:
            print("Your BMI is considered obese.")
    elif gender == 'F':
        if bmi < 23.0:
            print("Your BMI is considered underweight.")
        elif bmi >= 23.0 and bmi <= 27.0:
            print("Your BMI is considered normal weight.")
        elif bmi >= 27.1 and bmi <= 30.0:
            print("Your BMI is considered overweight.")
        else:
            print("Your BMI is considered obese.")
else:
    print("Invalid age input.")
