// https://programmers.co.kr/learn/courses/30/lessons/42839
#include <iostream>
#include <math.h>       /* sqrt */
#include <algorithm>    /* permutation */
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

#define MAX_LEN 10000000

bool isPrime[MAX_LEN];
bool check = false;

void makePrimeArray() {
    if (check == false) {
        fill_n(isPrime, MAX_LEN, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i < sqrt(MAX_LEN); i++) {
            if (isPrime[i] == false)
                continue;
            for (int j = i * i; j < MAX_LEN; j = j + i) {
                isPrime[j] = false;
            }
        }
        check = true;
    }
}

int solution(string numbers) {
    int answer = 0;
    vector<int> input;
    vector<int> visited;
    makePrimeArray();
    for (int i = 0; i < numbers.length(); i++) {
        input.push_back(i);
    }
    do {
        int count = 1;
        while (count <= input.size()) {
            string tmp;
            for (int i = 0; i < count; i++) {
                tmp.push_back(numbers[input.at(i)]);
            }
            auto it = find(visited.begin(), visited.end(), stoi(tmp));
            if (it == visited.end()) {
                visited.push_back(stoi(tmp));
                if (isPrime[stoi(tmp)]) {
                    answer++;
                    cout << tmp.c_str() << endl;
                }
            }
            count++;
        }
    } while(next_permutation(input.begin(), input.end()));

    return answer;
}

int main(void) {
    // cout << solution("17") << endl;
    // cout << solution("013") << endl;
    cout << solution("9011") << endl;
    return 0;
}