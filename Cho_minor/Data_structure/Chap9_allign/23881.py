len : int = int(input());

arr = list(input().split(sep = ','))

k : int = len
largest : int
largest_pos : int = 0
temp : int

for j in range(0, len - 1):
    largest =  int(arr[0])
    for i in range(0, len - 1 - j):
        if(int(arr[i]) >= largest):
            largest = int(arr[i]);
            largest_pos = i;
        arr[largest_pos] = arr[len - 1 - j];
        arr[len - j - 1] = largest;

for i in range(0, len):
    print(arr[i])