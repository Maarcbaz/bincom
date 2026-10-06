from data import colors
from collections import Counter

# frequency of most common color
frequency = Counter(colors)

most_common_color = frequency.most_common(1)[0][0]

print(f"The most common color: {most_common_color}")

# most won color
most_worn = frequency.most_common(1)[0][0]

print("The most worn color", most_worn)

# Median color

sorted_colors = sorted(colors)

median_color = sorted_colors[len(sorted_colors) // 2]

print("Median color:", median_color)

# Variance

import statistics

frequencies = list(frequency.values())

variance = statistics.pvariance(frequencies)

print("Variance:", round(variance, 2))


# Probability of selecting RED

red_count = frequency["RED"]
total_colors = len(colors)

probability_red = red_count / total_colors

print("Probability of red:", probability_red)
print("Percentage:", round(probability_red * 100, 2),"%")


# recursive research

def recursive_search(numbers, target, index=0):

    if index == len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return recursive_search(numbers, target, index + 1)


numbers = [10, 20, 30, 40, 50]

target = int(input("Enter a number: "))

result = recursive_search(numbers, target)

if result != -1:
    print("Number found at index:", result)
else:
    print("Number not found")

# Generate 4 random number

import random

binary_number = ""

for i in range(4):
    binary_number += str(random.randint(0, 1))

decimal_number = int(binary_number, 2)

print("Binary:", binary_number)


# fibonnacci first 50 numbers

fibonacci = []

a = 0
b = 1

for i in range(50):
    fibonacci.append(a)
    a, b = b, a + b

print(fibonacci)