# https://www.acmicpc.net/problem/1032

n = int(input())
strings = list()
result = ''
for i in range(n):
    strings.append(input())

for a in range(len(strings[0])):
    check = ''
    isCheck = True
    for b in range(len(strings)):
        if check == '':
            check = strings[b][a]
        else:
            if check != strings[b][a]:
                isCheck = False
    if not isCheck:
        result += '?'
    else:
        result += strings[b][a]


print(result)