""" In this program we will use strings and conditional statements to check for symptoms
"""
symptoms = str(input("Enter your symptoms (eg fever, headache, flu):" " ")).lower()

if symptoms == "fever":
    print("You may have an infection, rest and hydrate well.\n If symptoms get worse, contact gp")
elif symptoms == "headache":
    print("You may be dehydrated, hydrate and rest")
elif symptoms == "cough":
    print("You may have a flu or a cold, get some rest and stay hydrated")
else:
    print("Symptoms not recognized, Please enter the symptom again")