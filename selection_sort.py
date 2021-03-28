def selection_sort(n, arr):
    for i in range(n - 1):
        minn = i
        for j in range(i + 1, n):
            if arr[j] < arr[minn]:
                minn = j

        if minn != i:
            arr[minn], arr[i] = arr[i], arr[minn]


n = int(input())
arr = list(map(int, input().split()))
selection_sort(n, arr)
print(arr)
