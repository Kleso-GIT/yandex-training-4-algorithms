# https://contest.yandex.ru/contest/53032/problems/B/
def dino_checker(dinos, row, col):
    for r, c in dinos:
        if row == r or col == c or row + col == r + c or row - col == r - c:
            return False
    return True


def solve_n_dinos_util(n, dinos, col):
    if col == n:
        return 1
    count = 0
    for i in range(n):
        if dino_checker(dinos, i, col):
            dinos.append((i, col))
            count += solve_n_dinos_util(n, dinos, col + 1)
            dinos.pop()
    return count


def solve_n_dinos(n):
    dinos = []
    return solve_n_dinos_util(n, dinos, 0)


n = int(input())
count = solve_n_dinos(n)
print(count)
