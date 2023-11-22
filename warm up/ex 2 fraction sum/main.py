# Даны две рациональные дроби: a/b и c/d. Сложите их и результат представьте
# в виде несократимой дроби m/n.

def fraction_sum(a, b, c, d):

    def i_updating(divider, numerator):
        if numerator > divider:
            i = divider
        else:
            i = numerator
        return i

    divider = b * d
    numerator = a * d + b * c

    i = i_updating(divider, numerator)
    while i > 1:
        if divider % i == 0 and numerator % i == 0:
            divider /= i
            numerator /= i
            i = i_updating(divider, numerator)
        else:
            i -= 1

    return int(numerator), int(divider)


reader = open('input.txt', 'r')
a, b, c, d = [int(n) for n in reader.readline().split(" ")]
reader.close()

with open('output.txt', 'w') as output:
    res = fraction_sum(a, b, c, d)
    output.write(f"{res[0]} {res[1]}")
