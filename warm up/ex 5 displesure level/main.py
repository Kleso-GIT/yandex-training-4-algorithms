# https://contest.yandex.ru/contest/53027/problems/E/?success=95652364#30404/2023_02_12/FpB70IpgFh

n = int(input())
ratings = [int(rating) for rating in input().split(" ")]

res = []

lower_sum = 0
lower_len = 1
higher_sum = sum(ratings)
higher_len = len(ratings)

for student_index in range(n):
    lower_sum += ratings[student_index]

    weaker_students_displeasure = lower_len * ratings[student_index] - lower_sum
    stronger_students_displeasure = higher_sum - ratings[student_index] * higher_len

    lower_len += 1
    higher_len -= 1
    higher_sum -= ratings[student_index]

    res.append(str(weaker_students_displeasure + stronger_students_displeasure))

print(" ".join(res))
