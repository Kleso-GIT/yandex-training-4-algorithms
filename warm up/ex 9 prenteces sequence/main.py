# https://contest.yandex.ru/contest/53027/problems/I/

seq = input()


def is_correct(seq):
    stack = []
    for elem in seq:
        if not stack and elem in (")", "]", "}"):
            return "no"
        elif elem in ("(", "[", "{"):
            stack.append(elem)
        else:
            if elem == ")" and stack[-1] == "(":
                stack.pop()
            elif elem == "]" and stack[-1] == "[":
                stack.pop()
            elif elem == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return "no"
    if stack:
        return "no"
    return "yes"


print(is_correct(seq))
