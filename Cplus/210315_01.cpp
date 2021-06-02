// https://programmers.co.kr/learn/courses/30/lessons/43163
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
vector<int> answerList;
void bfs(string begin, string target, vector<string> words, int depth, int cnt, vector<string> visited) {
    visited.push_back(begin);
    if (depth == 0) {
        return;
    }
    if (begin.compare(target) == 0) {
        answerList.push_back(cnt);
        return;
    }
    for (string word : words) {
        if (find(visited.begin(), visited.end(), word) == visited.end()) {
            vector<bool> tmp;
            for (int i = 0; i < word.length(); i++) {
                if (begin[i] - word[i] == 0)
                    tmp.push_back(true);
                else
                    tmp.push_back(false);
            }
            if (count(tmp.begin(), tmp.end(), false) == 1) {
                bfs(word, target, words, depth - 1, cnt + 1, visited);
            }
        }
    }
    return;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    vector<string> visited;
    bfs(begin, target, words, words.size(), 0, visited);
    if (answerList.size() == 0) {
        answerList.push_back(0);
    }
    answer = *min_element(answerList.begin(), answerList.end());
    return answer;
}

int main(void) {
    cout << solution("hit", "cog", {"aaa"}) << endl;
    return 0;
}