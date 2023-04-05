import pandas as pd

# Input list of temperatures in Fahrenheit
temps_fahrenheit = [32, 50, 68, 77, 104]

# Write your code below to solve the challenge.
temps_celcius = pd.Series([(f - 32) * (5/9) for f in temps_fahrenheit], index=temps_fahrenheit)

print(f'max: {temps_celcius.max()}')
print(f'min: {temps_celcius.min()}')