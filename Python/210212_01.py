# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    answer_list = {}
    for i in clothes:
        if i[1] in answer_list:
            answer_list[i[1]].append(i[0])
        else:
            answer_list[i[1]] = []
            answer_list[i[1]].append(i[0])
    for i in answer_list:
        answer *= (len(answer_list[i]) + 1)
    answer -= 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3

"""
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
"""

"""
# https://www.daleseo.com/python-collections-counter/
Counter 기본 사용법 문서.
"""