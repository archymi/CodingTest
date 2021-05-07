# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations


def solution(nums):
    answer = 0
    orders = list(combinations(nums, 3))
    primeList = []

    def isPrime(a):
        if (a < 2):
            return False
        for i in range(2, a):
            if (a % i == 0):
                return False
        return True

    for i in range(2, 3001):
        if isPrime(i):
            primeList.append(i)

    for [a, b, c] in orders:
        if (a + b + c) in primeList:
            answer += 1

    return answer


solution([1, 2, 3, 4])
