height_in_cm = float (input("Enter your height in cm: "))

height_in_m = (height_in_cm / 100)  

height = height_in_m * height_in_m

weight = int (input("Enter your weight in kg: "))

BMI = float( weight / height)

print("your Body mass index is:", BMI)

if BMI < 18.5:
  print("You are underweight")

elif BMI >= 18.5 and BMI <= 24.9:
  print("You are normal")

elif BMI >= 25 and BMI <= 29.9 and BMI >= 30:
  print("You are overweight")
