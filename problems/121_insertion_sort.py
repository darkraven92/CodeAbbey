def insertion_sort_shifts():
    n = int(input())
    arr = list(map(int, input().split()))
    shift_counts = []

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        shifts = 0
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
        shift_counts.append(shifts)
    print(*shift_counts)

if __name__ == "__main__":
    insertion_sort_shifts()