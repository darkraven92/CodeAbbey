def selection_sort_indices():
    n = int(input())
    arr = list(map(int, input().split()))
    max_indices = []

    for i in range(n - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if arr[j] > arr[max_index]:
                max_index = j
        max_indices.append(max_index)
        arr[i], arr[max_index] = arr[max_index], arr[i]
    
    print(*max_indices)

if __name__ == "__main__":
    selection_sort_indices()