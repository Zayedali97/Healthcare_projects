""" This program will use functions to calculate the total cost of medications"""

# Medication database (Name: price in £).
medications = {
    'Paracetamol': 2.50,
    'Ibuprofen': 3.00,
    'Amoxicillin': 5.50,
    'Insulin': 25.00,
    'Aspirin': 2.00,
    'Metformin': 10.00
}

# Function to calculate the total cost of Medication.
def calculate_total_cost(prescription_list):
    total = 0
    for med in prescription_list:
        price = medications.get(med)
        if price:
            total += price
        else:
            print(f"Warning: {med} is not in the database. Skipped.")
    return total


# Get medication list from user
user_input = str(input("Enter the medications prescribed (separated by commas): "))
patient_prescription = [med.strip().title() for med in user_input.split(',')]

# Prints cleaned list
print("Processed meds:")
for med in patient_prescription:
    print(f"- '{med}'")

print("\nMedication entered: " + ", ".join(patient_prescription))
total_cost = calculate_total_cost(patient_prescription)

def apply_discount(total, discount_percentage):     # Function for discounts
    discount_amount = total_cost *(discount_percentage / 100)
    return total - discount_amount

# Asks if user has insurance for the discount to be applied

has_insurance = str(input("Does patient have insurance? yes/no: ")).strip().lower()
if has_insurance == "yes":
    total_cost = apply_discount(total_cost, 20)

patient_name = input("\nEnter the patients name: ")     # Asks for users name
print("\n--- Prescription Summary ---")
print(f"\nPatient: {patient_name}")
print("Medications:")

for med in patient_prescription:
    price = medications.get(med)
    if price:
        print(f"- {med}: £{price:.2f}")
    else:
        print(f"- {med}: Not Found")
if has_insurance == "yes":
    print("Insurance: Yes (20% discount applied)")
else:
    print("Insurance: No")
print(f"Final Total: £{total_cost:.2f}")
