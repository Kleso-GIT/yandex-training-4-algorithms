'''
Задана последовательность целых чисел a1, a2, …, an. Задаются запросы: сказать любой элемент
последовательности на отрезке от L до R включительно, не равный минимуму на этом отрезке.
'''


def input_reader(file):
    reader = open(file, 'r')
    reader.readline().split(" ")
    sequence = [int(n) for n in reader.readline().split(" ")]
    queries = []
    for line in reader:
        queries.append([int(n) for n in line.split(" ")])
    reader.close()
    return sequence, queries


def not_a_minimum(input_reader):
    sequence = input_reader[0]
    queries = input_reader[1]
    res = []
    for query in queries:
        start = query[0]
        end = query[1]
        query_slice = sequence[start:end + 1]
        query_slice.sort()
        if query_slice[-1] > query_slice[0]:
            res.append(query_slice[-1])
        else:
            res.append("NOT FOUND")
    return res


def output_writer(res):
    with open('output.txt', 'w') as output:
        for line in res:
            output.write(f"{line}\n")


output_writer(not_a_minimum(input_reader("input.txt")))


