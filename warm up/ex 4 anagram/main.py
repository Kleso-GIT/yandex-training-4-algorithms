# Задано две строки, нужно проверить, является ли одна анаграммой другой.
# Анаграммой называется строка, полученная из другой перестановкой букв.

str1 = input()
str2 = input()

if sorted([letter for letter in str1]) == sorted([letter for letter in str2]):
    print("YES")
else:
    print("NO")
