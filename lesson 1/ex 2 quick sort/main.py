# https://contest.yandex.ru/contest/53029/problems/B/

import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


n = int(input())
if n > 0:
    arr = input()
    arr = [int(num) for num in arr.split(" ")]
    print(" ".join([str(i) for i in quicksort(arr)]))
