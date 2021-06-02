# https://www.acmicpc.net/problem/14501
import copy

day = int(input())
work_list = list()
for i in range(day):
    a, b = map(int, input().split())
    work_list.append([a, b])

answerList = [0]

def dfs(now_day, target_day, works, visited, result):
    if now_day == target_day:
        answerList.append(result)

    for (idx, [during, money]) in enumerate(works):
        if (idx not in visited) and now_day <= idx:
            tmp = copy.deepcopy(visited)
            tmp.append(idx)
            dfs(idx + during, target_day, works, tmp, result + money)
        if idx + during > target_day:
            answerList.append(result)
            break


dfs(-1, day, work_list, list(), 0)
print(max(answerList))