# https://programmers.co.kr/learn/courses/30/lessons/49189
import collections

answerDict = dict()


def findHeight(str_tree: dict, now: int, depth: int):
    if now in str_tree:
        for a in str_tree[now]:
            if a not in answerDict:
                answerDict[a] = depth + 1
                print([a, depth + 1])

        for a in str_tree[now]:
            for b in str_tree[a]:
                if b not in answerDict:
                    findHeight(str_tree, a, answerDict[a])


def solution(n, edge):
    count = 0
    str_tree = dict()

    for [a, b] in edge:
        if a not in str_tree:
            str_tree[a] = list()
            str_tree[a].append(b)
        else:
            str_tree[a].append(b)

        if b not in str_tree:
            str_tree[b] = list()
            str_tree[b].append(a)
        else:
            str_tree[b].append(a)

    answerDict[1] = 0
    findHeight(str_tree, 1, 0)

    # print(answerDict)

    maxVal = max(answerDict.values())

    for a in answerDict.keys():
        if answerDict[a] == maxVal:
            count = count + 1
    return count


#print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(1, [[1, 2]]))
