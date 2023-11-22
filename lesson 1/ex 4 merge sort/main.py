# https://contest.yandex.ru/contest/53029/problems/D/

def merge_sort(arr):
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

        return res

    if len(arr) < 2:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    return merge(merge_sort(left), merge_sort(right))


n = int(input("n: "))
if n > 0:
    arr = [int(item) for item in input("array: ").split(" ")]
    print(" ".join([str(item) for item in merge_sort(arr)]))
