# https://www.acmicpc.net/problem/1107

btnCnt: int = 0
button = []
delButton = []
save: str = '100'

# 5457
target = str(input())

if len(target) > len(save):
    for i in range(len(target) - len(save)):
        save += '0'

if len(target) < len(save):
    tmp = ''
    for i in range(len(target)):
        tmp += save[i]
    save = tmp

# 3
delBtnCnt = int(input())
# 6 7 8
for i in map(int, input().split(' ')):
    delButton.append(i)

# 버튼이 없는 리모콘을 만든다.
for i in range(0, 10):
    if i not in delButton:
        button.append(i)

if save == target:
    print(0)
    exit(0)

for cnt, number in enumerate(target):
    # print("cnt: " + str(cnt) + " number: " + str(number) + " save: " + save)
    if cnt == 0:
        if 1 in button and target[0] == '1':
            continue
        else:
            if int(number) in button:
                tmp = list(save)
                tmp[cnt] = number
                save = ''.join(tmp)
                btnCnt = btnCnt + 1
            else:
                minimum = 10
                minimumIndex = 100
                for a, n in enumerate(button):
                    if abs(int(target[cnt]) - int(n)) < minimum:
                        minimum = abs(int(target[cnt]) - int(n))
                        minimumIndex = a
                tmp = list(save)
                tmp[cnt] = str(button[minimumIndex])
                save = ''.join(tmp)
                btnCnt = btnCnt + 1
    else:
        if int(number) in button:
            tmp = list(save)
            tmp[cnt] = number
            save = ''.join(tmp)
            btnCnt = btnCnt + 1
        else:
            minimum = 10
            minimumIndex = 100
            for a, n in enumerate(button):
                if abs(int(target[cnt]) - int(n)) < minimum:
                    minimum = abs(int(target[cnt]) - int(n))
                    minimumIndex = a

            tmp = list(save)
            tmp[cnt] = str(button[minimumIndex])
            save = ''.join(tmp)
            btnCnt = btnCnt + 1

# print(save)
btnCnt += min(abs(int(target) - int(save)), abs(int(target) + 10 - int(save)))

print(btnCnt)
