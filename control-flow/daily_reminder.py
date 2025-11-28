task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ") 

answer = ""
match priority.lower():
    case "high":
        answer = f"`{task}` is a high priority task that requires immediate attention today!"
    case "medium":
        answer = f"`{task}` is a medium priority task Try to get it done soon."
    case "low":
        answer = f"`{task}` is a low priority task. Consider completing it when you have free time."
    case _:
        answer = "Please enter a valid priority level: High, Medium, or Low."

if time_bound.lower() == "yes":
    print(f"Reminder: {answer}")
else:
    print(f"Note: {answer}")