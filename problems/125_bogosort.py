def random_generator(seed):
    x = seed
    while True:
        x_str = str(x).zfill(6)
        y_str = x_str[3:6] + x_str[0:3]
        y = int(y_str)
        x = (x * y)
        x_str = str(x).zfill(12)
        x = int(x_str[3:9])
        yield x


def shuffle(arr, rng):
    n = len(arr)
    for i in range(n):
        j = next(rng) % n
        arr[i], arr[j] = arr[j], arr[i]

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bogosort_with_limit(arr):
    rng = random_generator(918255)
    shuffles = 0
    max_shuffles = 10000

    while shuffles <= max_shuffles:
        if is_sorted(arr):
          return shuffles
        shuffle(arr,rng)
        shuffles += 1
    return -1


def solve_bogosort():
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        arr = list(map(int, input().split()))
        shuffles = bogosort_with_limit(arr)
        results.append(shuffles)
    print(*results)

if __name__ == "__main__":
    solve_bogosort()