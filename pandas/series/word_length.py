import pandas as pd

# Input list of words
words = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "strawberry"]

# Write your code below to solve the challenge.
words_length = pd.Series([len(word) for word in words], index=words)
mean = words_length.mean()
filtered_words = words_length[words_length >= mean]

print(filtered_words)
