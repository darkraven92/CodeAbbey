def count_lucky_tickets_advanced(n, b):
    if n % 2 != 0:
        raise ValueError("N must be even")
    half_n = n // 2
    
    max_digit_sum = half_n * (b - 1) #max sum

    dp_matrix = [[0]*(max_digit_sum + 1) for _ in range(half_n+1)]
    dp_matrix[0][0] = 1

    for digit_idx in range(1,half_n+1):
        for current_sum in range(max_digit_sum + 1):
            for digit_value in range(b):
                if current_sum >= digit_value:
                    dp_matrix[digit_idx][current_sum] += dp_matrix[digit_idx-1][current_sum - digit_value]
        
    total_lucky = 0
    for count in dp_matrix[half_n]:
        total_lucky += count**2


    return total_lucky


if __name__ == "__main__":
    n, b = map(int, input().split())
    lucky_count = count_lucky_tickets_advanced(n, b)
    print(lucky_count)