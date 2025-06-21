import numpy as np

# Student scores
score = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1 Average score per student
    # I used np.round so that I can round off the decimal in 2 digits
print(f"Average Score per Student:", np.round(score.mean(1),2))

# 2 Average score per subject
print(f"Average Score per Subject:", np.round(score.mean(0),2))

# 3 Student with the highest total score
print(f" Student with the Highest Total Score is:", score.sum(1).argmax())

# It shows that the 3rd row index student has the highest total = 277
   # [78, 85, 90],  # total = 253
   # [88, 79, 92],  # total = 259
   # [84, 76, 88],  # total = 248
   # [90, 93, 94],  # total = 277   highest
   # [75, 80, 70]   # total = 225

# 4 Adding 5 bonus points to 3rd Subject to all the Students
score[:, 2] = score[:, 2] + 5
print("Updated Score is:",score)
