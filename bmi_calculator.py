""" This program will request users to input weight and height 
to calculate Body Mass Index(BMI) and will categorize the result
"""


try:
        # Get user input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

        # Calculate BMI
    bmi = weight / (height ** 2)

        # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

        # Display result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
except ValueError:
    print("Please enter valid numeric values for weight and height.")
