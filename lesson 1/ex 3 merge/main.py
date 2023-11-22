# https://contest.yandex.ru/contest/53029/problems/C/

def merge(arr1, arr2):
    res = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res.extend(arr1[i:])
    res.extend(arr2[j:])

    return [str(item) for item in res]


n = int(input())
if n > 0:
    arr_n = [int(i) for i in input().split()]
else:
    input()
    arr_n = []
m = int(input())
if m > 0:
    arr_m = [int(i) for i in input().split()]
else:
    input()
    arr_m = []

print(" ".join(merge(arr_n, arr_m)))
