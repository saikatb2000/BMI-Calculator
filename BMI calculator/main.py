print("Welcome to BMI (Body Mass Index) calculator 2.0! (By Saikat)")
foot = float(input("Enter your hight in Foot: "))
# meter = foot/3.2808
meter = foot * 0.3048
meter = round(meter, 2)
print("Your hight in Meter is: ", meter)
height = float(meter)
weight = int(input("Enter Your Weight in Kg: "))
bmi = weight / (height*height)
bmi= round(bmi,2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif  bmi <25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif  bmi<30:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif  bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

