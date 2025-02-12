def solve():
    n = int(input())
    results = []

    for _ in range(n):
        line = input()
        numbers = list(map(int, line.split()))
        sum_of_squares = sum(x * x for x in numbers)
        results.append(sum_of_squares)

    print(*results)

solve()