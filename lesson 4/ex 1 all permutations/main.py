# https://contest.yandex.ru/contest/53032/problems/

def next_permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])


def all_permutations(nums):
    result = [nums.copy()]

    while True:
        next_permutation(nums)
        if nums == result[0]:
            break
        result.append(nums.copy())
    return result


n = int(input())
nums = [str(num + 1) for num in range(n)]
for perm in all_permutations(nums):
    print("".join(perm))
