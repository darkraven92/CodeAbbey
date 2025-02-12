def partition(arr, left, right):
    lt = left
    rt = right
    direction = 'left'
    pivot = arr[left]

    while lt < rt:
        if direction == 'left':
            if arr[rt] > pivot:
                rt -= 1
            else:
                arr[lt] = arr[rt]
                lt += 1
                direction = 'right'
        else:
            if arr[lt] < pivot:
                lt += 1
            else:
                arr[rt] = arr[lt]
                rt -= 1
                direction = 'left'
    arr[lt] = pivot
    return lt

def quicksort(arr, left, right, ranges):
    if left < right:
        pivot_pos = partition(arr, left, right)
        ranges.append(f"{left}-{right}")
        if pivot_pos - left > 1:
            quicksort(arr, left, pivot_pos - 1, ranges)
        if right - pivot_pos > 1:
            quicksort(arr, pivot_pos + 1, right, ranges)

def solve_quicksort():
    n = int(input())
    arr = list(map(int, input().split()))
    ranges = []
    quicksort(arr, 0, n - 1, ranges)
    print(*ranges)

if __name__ == "__main__":
    solve_quicksort()