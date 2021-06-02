# https://www.acmicpc.net/problem/1032

cnt = int(input())
save = ''
for i in range(cnt):
    tmp = input()
    if i == 0:
        save = tmp
    else:
        for j, k in enumerate(tmp):
            if save[j] == '?':
                continue
            if save[j] != tmp[j]:
                tmp1 = list(save)
                tmp1[j] = '?'
                save = ''.join(tmp1)

print(save)
