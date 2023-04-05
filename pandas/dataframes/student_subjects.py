import pandas as pd

# Input data
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
math_scores = [90, 80, 85, 88, 92]
science_scores = [89, 91, 80, 86, 95]
english_scores = [85, 88, 90, 92, 94]

# Write your code below to solve the challenge.
data = []

for i, student in enumerate(students):
    mean = (math_scores[i] + science_scores[i] + english_scores[i]) / 3
    data.append({
        'student': student,
        'math_score': math_scores[i],
        'science_score': science_scores[i],
        'english_score': english_scores[i],
        'mean': mean
    })

df = pd.DataFrame(data)
df.set_index('student', inplace=True)

print(df)
