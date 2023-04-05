import pandas as pd

# Input list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Write your code below to solve the challenge
squared = [x**2 for x in numbers]
even = [i for i in squared if i % 2 == 0]
series = pd.Series(even)

print(series.sum())