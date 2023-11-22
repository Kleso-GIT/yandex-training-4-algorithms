# https://contest.yandex.ru/contest/53029/problems/

n = int(input())
input_string = input()
if input_string:
    arr = [int(elem) for elem in input_string.split(" ")]
else:
    arr = []
x = int(input())


def partition(n, arr, x):
    '''
    :param n: arr length
    :param arr: list
    :param x: pivot
    :return: string where first num is count of elems lower then pivot and second number is num of elems greater
     or equal pivot
    '''
    low = 0
    high = n - 1

    count_lower_elems = 0

    if arr:

        while low <= high:
            if arr[low] < x:
                low += 1
                count_lower_elems += 1
            else:
                temp = arr[low]
                arr[low] = arr[high]
                arr[high] = temp
                high -= 1

    return f"{count_lower_elems} {n - count_lower_elems}"


print(partition(n, arr, x))
