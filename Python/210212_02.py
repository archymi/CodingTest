# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

def solution(genres, plays):
    answer = []
    count = {}
    sample = {}

    for index, item in enumerate(genres):
        if item not in count:
            count[item] = plays[index]
        else:
            count[item] += plays[index]
    countSort = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

    for index, item in enumerate(genres):
        if item not in sample:
            sample[item] = []
            sample[item].append([plays[index], index])
        else:
            sample[item].append([plays[index], index])
    for i in sample.keys():
        sample[i] = sorted(sample[i], key=lambda i: i[0], reverse=True)

    for i in countSort:
        for j in range(2):
            if len(sample[i]) >= 2:
                answer.append(sample[i][j][1])
            else:
                answer.append(sample[i][j][1])
                break


    return answer

"""
[ANSWER 01]
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

[ANSWER 02]
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play
"""

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]