def calculate_f(x, a_matrix, b_vector):
    n = len(x)
    f_values = []
    for i in range(n):
        f = 0
        for j in range(n):
            f += a_matrix[i][j] * x[j]
        f -= b_vector[i]
        f_values.append(f)
    
    result = 0
    for f in f_values:
      result += f*f
    return result


def calculate_gradient(x, dx, a_matrix, b_vector):
    n = len(x)
    y = calculate_f(x, a_matrix, b_vector)
    gradient = [0] * n
    
    for i in range(n):
        x_modified = x[:]
        x_modified[i] += dx
        y_modified = calculate_f(x_modified, a_matrix, b_vector)
        gradient[i] = (y_modified - y) / dx
        
    return gradient


def gradient_descent(a_matrix, b_vector):
    n = len(b_vector)
    x = [0.0] * n
    step = 0.01
    iteration = 0

    while True:
        y = calculate_f(x, a_matrix, b_vector)
        if y < 0.0001:
            break
            
        dx = step/10
        g = calculate_gradient(x, dx, a_matrix, b_vector)
        
        x_new = x[:]
        for i in range(n):
          x_new[i] -= g[i] * step
          
        y_new = calculate_f(x_new, a_matrix, b_vector)
        
        if y_new < y:
            x = x_new[:]
            step = min(0.1, step * 1.25)
        else:
            step = step / 1.25
            
        iteration += 1
    return iteration
    
def solve_linear_equations():
    num_systems = int(input())
    results = []
    for _ in range(num_systems):
        n = int(input())
        a_matrix = []
        for _ in range(n):
            row = list(map(float, input().split()))
            a_matrix.append(row)
        b_vector = list(map(float, input().split()))
        
        iterations = gradient_descent(a_matrix, b_vector)
        results.append(iterations)
    
    print(*results)

if __name__ == "__main__":
    solve_linear_equations()