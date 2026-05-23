
height_in_cm = float (input("Enter your height in cm: "))

height_in_m = float (height_in_cm / 100)  

height = float (height_in_m * height_in_m)

weight = float(input("Enter your weight in kg: "))

BMI = float( weight / height)

print("your Body mass index is:", BMI)

if BMI < 18.5:
  print("You are underweight")

elif BMI >= 18.5 and BMI <= 24.9:
  print("You are normal")

elif BMI > 25:
  print("You are overweight")
