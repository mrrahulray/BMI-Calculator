#version 2.0
print("Welcomto BMI calculator!")
name=input("What is your name:")
Height = float(input("Enter the height (miter): "))
Weight = float(input("Enter the weight (kg): "))

print(f"{name}, your Height is {Height} miter and weight is {int(Weight)} kg")


BMI = Weight/Height**2


if (BMI<18.5):
    print(f"Your BMI is {BMI}, you are Underweight")
elif (BMI>=18.5 and BMI<25):
    print(f"Your BMI is {BMI}, you have a normal weight")
elif (BMI>=25 and BMI<30):
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif (BMI>=30 and BMI<35):
    print(f"Your BMI is {BMI}, you are obese")
elif (BMI>=35):
    print(f"Your BMI is {BMI}, you are clinically obese")
