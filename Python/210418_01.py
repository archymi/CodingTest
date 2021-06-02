# https://www.acmicpc.net/problem/1041

three_possible = [
    [1, 2, 3], [2, 3, 6], [3, 5, 6], [1, 3, 5],
    [1, 2, 4], [1, 4, 5], [2, 4, 6], [4, 5, 6]
]

two_possible = [
    [1, 2], [1, 3], [1, 4], [1, 5],
    [2, 3], [2, 4], [2, 6],
    [3, 5], [3, 6],
    [4, 5], [4, 6],
    [5, 6]
]

num = int(input())
dice_input = list(map(int, input().split()))

dice = list()
dice.append(0)
for i in dice_input:
    dice.append(i)

three_possible_list = []
two_possible_list = []

for [a, b, c] in three_possible:
    three_possible_list.append(dice[a] + dice[b] + dice[c])

for [a, b] in two_possible:
    two_possible_list.append(dice[a] + dice[b])

min_three = min(three_possible_list)
min_two = min(two_possible_list)
min_one = min(dice[1:])


if num == 1:
    print(sum(dice) - max(dice))
elif num == 2:
    print(min_three * 4 + min_two * 4)
else:
    # 1 층
    one_floor = min_two * 4 + min_one * (num-2) * 4
    # N 층
    n_floor = min_three * 4 + min_two * (num-2) * 4 + min_one * (num-2) * (num-2)
    # 1 ~ N 층 사이
    middle_floor = min_two * 4 + min_one * (num-2) * 4
    # 결과
    answer = one_floor + n_floor + middle_floor * (num-2)
    print(answer)