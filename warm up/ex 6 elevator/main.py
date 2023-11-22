# https://contest.yandex.ru/contest/53027/problems/F/

k = int(input())
n = int(input())
a = []
for _ in range(n):
    elem = int(input())
    a.append(elem)

res = 0
while a:
    if a[-1] == 0:
        a.pop()
    else:
        break

while a:
    places = k

    if a[-1] == 0:
        a.pop()
        continue

    res += len(a) * 2

    while places > 0 and a:

        if a[-1] <= places:
            places -= a[-1]
            a.pop()
        else:
            if places == k:
                rides = a[-1] // k
                res += len(a) * 2 * rides - len(a) * 2
                if k * rides % a[-1] > 0:
                    a[-1] -= rides * places
                else:
                    a.pop()
                places = 0
            else:
                a[-1] -= places
                places = 0
print(res)
