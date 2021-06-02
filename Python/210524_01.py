# https://www.acmicpc.net/problem/1976

parent = dict()
map_info = list()

n = int(input())

for i in range(0, 201):
    parent[i] = -1


def find(x):
    if parent[x] < 0:
        return x
    y = find(parent[x])
    parent[x] = y
    return y


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

m = int(input())

for i in range(n):
    map_info.append(list(map(int, input().split())))
    for j in range(n):
        if map_info[i][j] != 0:
            union(i, j)

travel_info = list(map(int, input().split()))
start = find(travel_info[0] - 1)
check = True
for i in travel_info:
    if start != find(i-1):
        check = False
        break
if check:
    print("YES")
else:
    print("NO")
