# Read the input as a single line
input_data = input().split()

# The first value is the number of temperatures
num_temps = int(input_data[0])

# The rest are the Fahrenheit temperatures
fahrenheit_temps_str = input_data[1:]

# Initialize an empty list to store the Celsius temperatures
celsius_temps = []

# Loop through each Fahrenheit temperature
# Limited to the number of temperatures
for i in range(num_temps):
    # Convert the temperature string to an integer
    f = int(fahrenheit_temps_str[i])

    # Convert Fahrenheit to Celsius using the formula
    c = (f - 32) * 5 / 9

    # Round the Celsius temperature using "half away from zero" rounding
    if c >= 0:
        rounded_c = int(c + 0.5)
    else:
        rounded_c = int(c - 0.5)

    # Add the rounded result to the list
    celsius_temps.append(rounded_c)

# Print the Celsius temperatures separated by spaces
print(*celsius_temps)
