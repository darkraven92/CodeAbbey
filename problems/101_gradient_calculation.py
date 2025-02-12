import math

def calculate_gradient(x, y, A, B, C):
    exp_term = math.exp(- (x + A)**2 - (y + B)**2)
    df_dx = 2 * (x - A) - 2 * C * (x + A) * exp_term
    df_dy = 2 * (y - B) - 2 * C * (y + B) * exp_term
    return df_dx, df_dy

def direction_of_descent(x, y, A, B, C):
    df_dx, df_dy = calculate_gradient(x, y, A, B, C)
    theta = math.atan2(-df_dy, -df_dx)  # Negative for descent
    degrees = math.degrees(theta)
    if degrees < 0:
        degrees += 360
    return round(degrees)

if __name__ == "__main__":
    try:
        first_line = input().split()
        num_points = int(first_line[0])
        A = float(first_line[1])
        B = float(first_line[2])
        C = float(first_line[3])
        
        points = []
        for _ in range(num_points):
            line = input().split()
            try:
                x = float(line[0])
                y = float(line[1])
                points.append((x, y))
            except (IndexError, ValueError):
               print(f"Skipping invalid point line: {line}")
               continue

        for x, y in points:
            print(direction_of_descent(x, y, A, B, C), end=' ')
        print() #add a new line at the end to make the terminal more clear
            
    except ValueError:
        print("Invalid input. Please ensure all input is numeric in format: num_points A B C on first line, and x y per line after")
    except IndexError:
       print("Invalid input. Please ensure input contains num_points, A, B and C in the first line")