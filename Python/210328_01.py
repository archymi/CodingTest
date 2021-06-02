# https://www.acmicpc.net/problem/1010
sol = dict()
sol[0] = 1
sol[1] = 1

def factorial(number : int) :
    if number in sol:
        return sol[number]
    else:
        sol[number] = number * factorial(number - 1)

    return sol[number]


cnt = int(input())
for i in range(cnt):
    a, b = map(int, input().split(' '))
    print(int(factorial(b) / (factorial(b-a) * factorial(a))))