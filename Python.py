# Get score from user
score = float(input("Enter student's score: "))

# Grading logic
if 70 <= score <= 100:
    print("Grade: A")
elif 60 <= score <= 69:
    print("Grade: B")
elif 50 <= score <= 59:
    print("Grade: C")
elif 45 <= score <= 49:
    print("Grade: D")
elif 40 <= score <= 44:
    print("Grade: E")
elif 0 <= score < 40:
    print("Grade: F")
else:
    print("Invalid score")
