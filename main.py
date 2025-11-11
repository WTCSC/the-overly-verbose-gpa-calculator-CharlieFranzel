
print("Welcome to the calc (thats slang for calculator)")

# Collect grades
grades = []
num_classes = int(input("How many classes are you in? "))

for i in range(num_classes):
    while True:
        try:
            g = float(input(f"Enter grade {i+1} (0.0-4.0): "))
            if 0.0 <= g <= 4.0:
                grades.append(g)
                break
            else:
                print("Grade must be between 0.0 and 4.0.")
        except:
            print("Invalid input. Please enter a number.")

# Current GPA
current_gpa = sum(grades) / len(grades)
print(f"Your current GPA is: {round(current_gpa, 2)}")

# Semester analysis
print("Which semester do you want to analyze?")
print("1. First half")
print("2. Second half")
choice = input("Enter 1 or 2: ")

mid = len(grades) // 2
if choice == "1":
    sem = grades[:mid]
else:
    sem = grades[mid:]

sem_gpa = sum(sem) / len(sem)
print(f"Semester GPA: {round(sem_gpa, 2)}")

if sem_gpa > current_gpa:
    print("You improved!")
elif sem_gpa < current_gpa:
    print("You declined.")
else:
    print("You stayed the same.")

# Goal GPA
while True:
    try:
        goal = float(input("Enter your goal GPA (0.0-4.0): "))
        if 0.0 <= goal <= 4.0:
            break
        else:
            print("Goal must be between 0.0 and 4.0.")
    except:
        print("Invalid input.")

# Check if one grade can be raised to hit goal
possible = False
for i in range(len(grades)):
    new_list = grades.copy()
    new_list[i] = 4.0
    new_gpa = sum(new_list) / len(new_list)
    if new_gpa >= goal:
        print(f"You can reach your goal by raising class {i+1} to 4.0")
        possible = True

if goal <= current_gpa:
    print("You already meet or exceed your goal!")
elif not possible:
    print("You cannot reach your goal by raising just one grade.")
