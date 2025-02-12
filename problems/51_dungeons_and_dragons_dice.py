from collections import Counter
import itertools
import math

# Precompute the expected distributions for all possible dice combinations
def generate_distribution(num_dice, num_sides):
    # The sum of dice follows a multinomial distribution
    # We can use the convolution of the individual dice distributions
    distribution = [1] * num_sides
    for _ in range(1, num_dice):
        new_distribution = [0] * (len(distribution) + num_sides)
        for i in range(len(distribution)):
            for j in range(num_sides):
                new_distribution[i + j] += distribution[i]
        distribution = new_distribution
    return distribution

# Calculate the expected distribution for all possible combinations
expected_distributions = {}
for num_dice in range(1, 6):
    for num_sides in [2, 4, 6, 8, 10, 12]:
        expected_distributions[(num_dice, num_sides)] = generate_distribution(num_dice, num_sides)

# Function to calculate the frequency distribution of the sums
def calculate_frequency_distribution(sums):
    return Counter(sums)

# Function to calculate the mean and variance of the sums
def calculate_mean_and_variance(sums):
    mean = sum(sums) / len(sums)
    variance = sum((x - mean) ** 2 for x in sums) / len(sums)
    return mean, variance

# Function to compare the observed distribution with the expected distributions
def find_best_match(observed_distribution, observed_mean, observed_variance):
    min_distance = float('inf')
    best_match = None
    for (num_dice, num_sides), expected_distribution in expected_distributions.items():
        # Calculate expected mean and variance
        expected_mean = num_dice * (num_sides + 1) / 2
        expected_variance = num_dice * (num_sides ** 2 - 1) / 12
        # Calculate the distance between observed and expected mean and variance
        distance = abs(observed_mean - expected_mean) + abs(observed_variance - expected_variance)
        if distance < min_distance:
            min_distance = distance
            best_match = (num_dice, num_sides)
    return best_match

# Read the input data
input_data = """
8 17 13 13 15 16 12 6 15 15 14 9 14 11 12 9 13 12 12 12 15 9 14 13 13 14 7 13 15 16 14 12 15 11 12 14 12 12 11 12 14 12 12 11 13 13 14 11 15 10 10 13 11 12 14 13 18 12 15 12 15 11 13 17 11 11 9 14 12 15 15 13 12 16 13 11 11 10 13 14 9 14 9 13 12 11 12 12 14 14 8 16 12 10 13 17 12 13 14 11 0
12 16 12 12 15 13 12 11 11 14 13 14 11 15 8 9 13 13 9 13 9 12 13 8 6 16 15 6 11 16 14 8 13 10 19 10 13 14 12 10 13 13 16 14 13 11 10 12 16 14 14 14 13 7 8 12 8 14 9 11 10 14 14 12 15 11 15 13 12 13 13 11 9 10 8 9 9 6 15 13 18 15 14 9 12 12 13 10 10 14 9 10 15 14 12 9 17 10 16 10 0
7 10 6 7 8 7 7 8 6 7 8 6 7 6 8 8 7 7 6 8 6 9 7 7 8 7 9 9 8 7 5 8 7 9 9 8 7 7 7 8 9 7 7 7 9 7 7 6 7 6 8 8 7 8 7 9 8 9 8 9 5 7 8 8 8 9 10 7 7 6 6 6 7 9 7 8 8 9 7 8 7 8 7 7 6 6 8 10 6 8 9 8 7 9 8 6 10 8 8 7 0
"""
sums = [int(x) for x in input_data.split() if x != '0']

# Split the sums into three lines
line1 = sums[:100]
line2 = sums[100:200]
line3 = sums[200:300]

# Calculate the frequency distribution, mean, and variance for each line
freq1 = calculate_frequency_distribution(line1)
mean1, var1 = calculate_mean_and_variance(line1)
freq2 = calculate_frequency_distribution(line2)
mean2, var2 = calculate_mean_and_variance(line2)
freq3 = calculate_frequency_distribution(line3)
mean3, var3 = calculate_mean_and_variance(line3)

# Find the best match for each line
match1 = find_best_match(freq1, mean1, var1)
match2 = find_best_match(freq2, mean2, var2)
match3 = find_best_match(freq3, mean3, var3)

# Output the results
print(f"{match1[0]}d{match1[1]} {match2[0]}d{match2[1]} {match3[0]}d{match3[1]}")