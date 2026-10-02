print("Student Grade Calculator")

name = input("Enter student name: ")

marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))
marks4 = float(input("Enter marks of Subject 4: "))
marks5 = float(input("Enter marks of Subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
