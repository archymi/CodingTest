# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

def solution(n, results):
    answer = 0
    winner_ = dict()
    loser_ = dict()

    for man in range(1, n+1):
        winner_[man] = []
        loser_[man] = []

    for [winner, loser] in results:
        winner_[winner].append(loser)
        loser_[loser].append(winner)

    print(winner_)
    print(loser_)

    check = True
    while check:
        check = False
        for man in range(1, n+1):
            # loser : man 이 진 상대들, 더썐놈
            for loser in loser_[man]:
                # winner : man 이 이긴 상대들, 더 약한놈
                for winner in winner_[man]:
                    if winner not in winner_[loser]:
                        winner_[loser].append(winner)
                        check = True
                    if loser not in loser_[winner]:
                        loser_[winner].append(loser)
                        check = True
                        
                    

    for man in range(1, n+1):
        if len(winner_[man]) + len(loser_[man]) == (n-1):
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2