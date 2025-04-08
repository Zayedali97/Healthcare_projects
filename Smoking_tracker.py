""" This is a program that keeps track of smoking/vape entries for people who want to quite smoking/vaping
"""

import datetime

# Function to log a vape entry
def log_vape_entry(logs):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reason = input("What triggered the craving? (e.g. boredom, stress, habit): ")
    strength = input("How strong was the urge (1–10)? ")
    logs.append({"time": time, "reason": reason, "strength": strength})
    print("Entry logged.\n")

# Function to show summary
def show_summary(logs):
    print("\n--- Vape Log Summary ---")
    print(f"Total entries today: {len(logs)}")
    for entry in logs:
        print(f"{entry['time']} - Reason: {entry['reason']} | Strength: {entry['strength']}")
        print("------------------------\n")

# Main program loop
vape_logs = []

while True:
    print("1. Log a craving")
    print("2. Show today’s summary")
    print("3. Quit")

    choice = input("Select an option (1-3): ")

    if choice == "1":
        log_vape_entry(vape_logs)
    elif choice == "2":
        show_summary(vape_logs)
    elif choice == "3":
        print("Stay strong, Zayed. You’ve got this.")
        break
    else:
        print("Invalid option. Try again.\n")
