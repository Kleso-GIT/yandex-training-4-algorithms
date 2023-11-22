'''
Дана строка S, состоящая из строчных латинских букв.
Определите, совпадают ли строки одинаковой длины L, начинающиеся с позиций A и B.
'''

# https://contest.yandex.ru/contest/53030/problems/A/

s = input()
q = int(input())
queries = []
for query in range(q):
    queries.append([int(num) for num in input().split(" ")])

# Предподготовка за O(N)
n = len(s)
p = 10 ** 9 + 7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = " " + s
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p


# Сравнение
def isequal(slen, from1, from2):
    return (
            (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p
    )


for query in queries:
    if isequal(query[0], query[1] + 1, query[2] + 1):
        print("yes")
    else:
        print("no")
