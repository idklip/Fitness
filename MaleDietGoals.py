
# def

def double(a):
    return "%.2f" % round(a, 2)

# Input Variables

name = input("Name: ")

weight = int(input("Weight (lbs): "))

height_f = int(input("Height (Feet): "))
height_i = int(input("Height (Inches): "))

age = int(input("Age: "))

actLvl = int(input("   Activity Levels\n"
               "0. Basal Metabolic Rate (BMR) \n"
               "1. Sedentary (Little or no exercise, <1,000 steps) \n"
               "2. Light (Exercise/Lifting 1-3 times/week; 1,000-10,000 steps/day; <4 miles) \n"
               "3. Moderate (Exercise/Lifting 4-5 times/week; 10,000-16,000 steps/day; 4-8 miles) \n"
               "4. Active (Exercise/Lifting 4-6 times/week + cardio; 17,000-23,000 steps/day; 8-12 miles) \n"
               "5. High (Sports/Labor Daily; 23,000+ steps/day; 12+ miles) \n"
               "Your Activity Level: "))


# Calculable Variables

# BMR
w = float(weight / 2.2)
h = float(((height_f * 12) + height_i) * 2.54)
bmr = int(10*w + 6.25*h - 5*age) + 5

if actLvl == 0:
    multi = 1

elif actLvl == 1:
    multi = 1.2

elif actLvl == 2:
    multi = 1.375

elif actLvl == 3:
    multi = 1.55

elif actLvl == 4:
    multi = 1.725

elif actLvl == 5:
    multi = 1.9

else:
    print("error")

fmr = bmr * multi

# Optimal Caloric Modifier

d = input("Are you looking to cut, maintain, or bulk? (c/m/b): ")

if d == "c":
    c = int(input("How much weight are you looking to lose? (lbs): "))
    t = int(input("How long do you plan on dieting for? (weeks): "))
    mod = (c / t) * 500
    fmr = fmr - mod
    name += "_cut"

elif d == "m":
    mod = 0
    fmr = fmr + mod
    name += "_maintain"

elif d == "b":
    b = float(input("How much do you plan to gain in body weight per week? (lbs): "))
    mod = b * 500
    fmr = fmr + mod
    name += "_bulk"

else:
    print("error")

# Macros

fatLvl = int(input("   Desired Level of Dietary Fat\n"
               "1. Minimal \n"
               "2. A Little \n"
               "3. Average \n"
               "4. More \n"
               "5. High \n"
               "Dietary Fat Level: "))

if fatLvl == 1:
    div = 0.3

elif fatLvl == 2:
    div = 0.35

elif fatLvl == 3:
    div = 0.4

elif fatLvl == 4:
    div = 0.45

elif fatLvl == 5:
    div = 0.5

else:
    print("error")


protein = int(w * 2.2 * .8)

procal = protein * 4

fat = int(div * weight)

fatcal = fat * 9

carbcal = fmr - fatcal - procal

carb = int(carbcal / 4)

# Output
name += ".txt"

output = "\nDaily Calories: " + str(int(fmr)) + "\n" + \
         "Protein Intake: " + str(protein) + "g\n" + \
         "Carb Intake: " + str(carb) + "g\n" + \
         "Fat Intake: " + str(fat) + "g\n"

print(output)

f = input("Print Info to file? (y/n): ")

if f == "y":
    with open(name, 'a') as file:
        file.write(output)
    print(f"Info has been saved to {name}")

elif f == "n":
    print("Info not saved")

else:
    print("error")

# Move-Item -Path .\*.txt -Destination C:\Users\honde\workspace\PersonalProjects\Fitness\TextFiles
