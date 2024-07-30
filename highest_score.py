"""
Write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
"""
# Input a list of student scores
student_scores = input().split()
scores_list = []
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
  scores_list.append(student_scores[n])
  
scores_list.sort()
highest_score = scores_list[-1]
print(f"The highest score in the class is: {highest_score}")
