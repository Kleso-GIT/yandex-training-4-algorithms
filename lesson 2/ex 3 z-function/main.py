# https://contest.yandex.ru/contest/53030/problems/C/

def calculate_z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z

s = input()

z_function_values = calculate_z_function(s)

print(" ".join(map(str, z_function_values)))
