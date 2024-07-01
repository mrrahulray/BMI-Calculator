# Simple BMI calculator
#description:
# BMI= Body Mass Index
# formula = (weight/(height^2))
print("Welcomto BMI calculator!")
name=input("What is your name:")
Height = float(input("Enter the height (miter): "))
Weight = float(input("Enter the weight (kg): "))

print(f"{name}, your Height is {Height} miter and weight is {int(Weight)} kg")


BMI = Weight/Height**2
print(f"Your BODY mask index (BMI) is {int(BMI)}")