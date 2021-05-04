# https://programmers.co.kr/learn/courses/30/lessons/49189
import collections

def solution(n, edge):
    str_tree = dict()
    answer_dict = dict()

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


    que = collections.deque()

    que.append(1)
    answer_dict[1] = 0
    while que:
        num = que.popleft()
        for a in str_tree[num]:
            if a not in answer_dict:
                answer_dict[a] = answer_dict[num] + 1
                que.append(a)

    print(answer_dict)
    answer_list = list(answer_dict.values())
    maxVal = max(answer_list)
    return answer_list.count(maxVal)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))