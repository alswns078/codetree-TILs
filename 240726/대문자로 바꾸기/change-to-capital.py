arr = []

for i in range(5):
    arr.append(list(input().split()))

arr2 = []
for i in arr:
    for item in i:
        arr2.append(item.upper())

chk = 0
for i in arr2:
    chk += 1
    print(i, end=" ")
    if chk % 3 == 0:
        print()