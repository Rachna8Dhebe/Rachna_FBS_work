num_students = int(input("Enter number of students: "))
total_percentages = 0  # To calculate average later

for student in range(1, num_students + 1):
    print(f"\nEnter marks for Student {student}:")
    total_marks = 0

    for subject in range(1, 6):
        marks = float(input(f"  Subject {subject} marks: "))
        total_marks += marks

    percentage = total_marks / 5
    total_percentages += percentage
    print(f"Percentage of Student {student}: {percentage:.2f}%")

average = total_percentages / num_students
print(f"\nAverage Percentage of all students: {average:.2f}%")
