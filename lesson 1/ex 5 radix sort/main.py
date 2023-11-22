# https://contest.yandex.ru/contest/53029/problems/E/

n = int(input())
array = []

for i in range(n):
    array.append(input())

print("Initial array:")
print(", ".join(array))
print("**********")

for phase in range(len(str(array[0]))):
    buckets = [[], [], [], [], [], [], [], [], [], []]

    print(f"Phase {phase + 1}")

    for num in array:
        reminder = (int(num) % (10 ** (phase + 1))) // 10 ** phase
        buckets[reminder].append(num)

    for bucket_index in range(len(buckets)):
        if buckets[bucket_index]:
            elem = ", ".join(buckets[bucket_index])
        else:
            elem = "empty"
        print(f"Bucket {bucket_index}: {elem}")

    array = []
    for bucket in buckets:
        array.extend(bucket)

    print("**********")

print("Sorted array:")
print(", ".join(array))
