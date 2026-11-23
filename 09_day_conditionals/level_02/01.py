# Write a code which gives grade to students according to theirs scores
# Output:
  # 90-100, A
  # 80-89, B
  # 70-79, C
  # 60-69, D
  # 0-59, F

score = int(input("Enter the student's score (0-100): "))
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score. Please enter a score between 0 and 100.")