# Всего студентов по направлению «Мировая культура» — n человек. Преподаватель дал задание — групповой проект.
# Для выполнения этого задания студенты должны разбиться на группы численностью от a до b человек.
# Скажите, можно ли разбить всех студентов на группы для выполнения проекта или преподаватель что-то перепутал.

t = int(input())
cases = []
for _ in range(t):
    cases.append(list(map(int, input().split())))


def is_divisible(n, a, b):
    if n % a <= (n // a) * (b - a):
        return "YES"
    else:
        return "NO"


for case in cases:
    print(is_divisible(case[0], case[1], case[2]))
