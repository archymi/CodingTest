// https://programmers.co.kr/learn/courses/30/lessons/43164
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
vector<vector<string>> answerList;

void bfs(vector<vector<string>> tickets, vector<string> answer,
         vector<bool> visited) {
    if (tickets.size() + 1 == answer.size()) {
        answerList.push_back(answer);
        return;
    }

    for (int i = 0; i < tickets.size(); i++ ) {
        if (answer.size() == 0) {
            if (tickets[i][0] == "ICN") {
                vector<string> tmp = answer;
                vector<bool> visitedtmp = visited;
                cout << tickets[i][0] << ", " << tickets[i][1] << " depth: " << answer.size() <<endl;
                tmp.push_back(tickets[i][0]);
                tmp.push_back(tickets[i][1]);
                visitedtmp[i] = true;
                bfs(tickets, tmp, visitedtmp);
            }
        } else {
            if (!visited[i]) {
                if (tickets[i][0] == answer[answer.size() - 1]) {
                    cout << tickets[i][0] << ", " << tickets[i][1] << " depth: " << answer.size() <<endl;
                    vector<string> tmp = answer;
                    vector<bool> visitedtmp = visited;
                    tmp.push_back(tickets[i][1]);
                    visitedtmp[i] = true;
                    bfs(tickets, tmp, visitedtmp);
                }
            }
        }
    }

    return;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    vector<bool> visited;
    for (int i = 0; i < tickets.size() + 1; i++ ) {
        visited.push_back(false);
    }

    bfs(tickets, answer, visited);

    sort(answerList.begin(), answerList.end());

    answer = answerList[0];
    for (auto a : answer) {
        cout << a << ", ";
    }
    cout << endl;
    return answer;
}

int main() {
    // solution({{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}});
    // solution({{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL", "SFO"}});
    // solution({{"ICN", "A"}, {"A", "B"}, {"B", "G"}, {"G", "B"}, {"B", "C"}});
    // solution({{"ICN", "A"}, {"A", "B"}, {"B", "G"}, {"B", "C"}, {"C", "B"}});
    solution({{"ICN", "A"}, {"ICN", "A"}, {"ICN", "A"}, {"A", "INC"}, {"A", "INC"}, {"A", "CDD"}});
    return 0;
}