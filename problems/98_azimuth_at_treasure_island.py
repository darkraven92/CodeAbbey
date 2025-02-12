import math

def calculate_treasure_coordinates(directions):
    x, y = 0, 0  # Start at the origin
    
    for line in directions:
        if line.startswith("go"):
            parts = line.split()
            distance = int(parts[1])  # Extract distance (index 1)
            azimuth = int(parts[5])   # Extract azimuth (index 5)
            
            # Convert azimuth to radians
            azimuth_rad = math.radians(azimuth)
            
            # Calculate delta_x and delta_y
            delta_x = distance * math.sin(azimuth_rad)
            delta_y = distance * math.cos(azimuth_rad)
            
            # Update position
            x += delta_x
            y += delta_y
    
    # Round to nearest integers
    x = round(x)
    y = round(y)
    
    return x, y

# Read input from the terminal
print("Enter the directions (type 'Dig here!' to finish):")
directions = []
while True:
    line = input().strip()
    directions.append(line)
    if line == "Dig here!":
        break

# Calculate and print the result
x, y = calculate_treasure_coordinates(directions)
print(f"Treasure coordinates: {x} {y}")