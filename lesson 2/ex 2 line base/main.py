# https://contest.yandex.ru/contest/53030/problems/B/

def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def min_period_length(s):
    pi = prefix_function(s)
    return len(s) - pi[-1]


input_string = input().strip()

print(min_period_length(input_string))
