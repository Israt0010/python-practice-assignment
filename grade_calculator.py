#1. Takes a student's name as input
student_name = input("Enter the student's name: ")

print()
#2. Takes marks for three subjects
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))

print()
#3. Calculates the average mark
average = (math + english + python) / 3

print()

#4. Determines the grade using the following conditions
if average >= 80:
    grade = 'A+'
elif average >= 70:
    grade = 'A'
elif average >= 60:
    grade = 'A-'
elif average >= 50:
    grade = 'B'
elif average >= 40:
    grade = 'C'
else:
    grade = 'F'

print()
#5. Display the student's name, average marks, and final grade
print()
print(f"Student Name: {student_name}")
print(f"Average Marks: {average:.2f}")
print(f"Final Grade: {grade}")

print()
#6. If any subject mark is below 0 or above 100, display an invalid marks message
if math < 0 or math > 100 or english < 0 or english > 100 or python < 0 or python > 100:
    print("Invalid marks!")   