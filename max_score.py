"""Several ways to get the highest value"""
student_scores = [180, 124, 165, 173, 189, 169, 146]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

"""Alternative two"""
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
student_scores.sort()
print(student_scores[-1])

"""Alternative three"""
student_scores = [180, 124, 165, 173, 189, 169, 146]
print(max(student_scores))
