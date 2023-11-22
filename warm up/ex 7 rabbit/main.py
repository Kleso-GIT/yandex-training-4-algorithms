# Помогите кролику найти сторону квадрата наибольшей площади, заполненного морковками полностью.
# https://contest.yandex.ru/contest/53027/problems/G/

n, m = map(int, input().split())
bed = [[] for _ in range(n)]

for i in range(n):
    bed[i].extend(map(int, input().split()))

max_side_length = 0

if bed:
    for row in range(0, n):
        for column in range(0, m):
            if bed[row][column] == 0:
                bed[row][column] = 0
            else:
                if row - 1 >= 0 and column - 1 >= 0:
                    bed[row][column] = min(bed[row - 1][column],
                                                      bed[row - 1][column - 1],
                                                      bed[row][column - 1]) + 1
                else:
                    bed[row][column] = 1

            if bed[row][column] > max_side_length:
                max_side_length = bed[row][column]

print(max_side_length)
