import sys

len = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split(sep = ' '))

rdy : bool
i : int
j : int
tmp : int
swap : int = 0

for i in range(0, len):
    arr[i] = int(arr[i])

for i in range(0, len):
    rdy = 1
    for j in range(0, len - i - 1):
        tmp = arr[j]
        if(arr[j] > arr[j + 1]):
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
            rdy = 0

    if(rdy == 1):
        break

print(j)