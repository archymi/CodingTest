# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    result = ''
    left_hand = [0, 0]
    right_hand = [2, 0]

    def pathLength(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def numPosition(num):
        if num == 1:
            return [0, 3]
        elif num == 2:
            return [1, 3]
        elif num == 3:
            return [2, 3]
        elif num == 4:
            return [0, 2]
        elif num == 5:
            return [1, 2]
        elif num == 6:
            return [2, 2]
        elif num == 7:
            return [0, 1]
        elif num == 8:
            return [1, 1]
        elif num == 9:
            return [2, 1]
        elif num == 0:
            return [1, 0]

    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left_hand = numPosition(num)
        elif num in [3, 6, 9]:
            result += 'R'
            right_hand = numPosition(num)
        elif num in [2, 5, 8, 0]:
            tmp = numPosition(num)
            if pathLength(tmp, left_hand) > pathLength(tmp, right_hand):
                result += 'R'
                right_hand = numPosition(num)
            elif pathLength(tmp, left_hand) == pathLength(tmp, right_hand):
                if hand == 'right':
                    result += 'R'
                    right_hand = numPosition(num)
                else:
                    result += 'L'
                    left_hand = numPosition(num)
            else:
                result += 'L'
                left_hand = numPosition(num)
    return result

#print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
#print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
#print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 5, 8, 2], 'right'))