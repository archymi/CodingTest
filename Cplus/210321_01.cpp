// https://programmers.co.kr/learn/courses/30/lessons/43238?language=cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
long long tmp;

void binarySearch(long long start, long long end, int n, vector<int> times) {
    long long sum = 0;
    long long middle = ( start + end ) / 2;
    for(auto i : times) {
        sum += middle / i;
    }
    cout << start << ", " << end << ", " << middle << ", " << sum << endl;
    if (start > end) {
        tmp = middle + 1;
        return;
    }
    if (sum < n) {
        binarySearch(middle+1, end, n, times);
    } else {
        binarySearch(start, middle-1, n, times);
    }
    return;
}

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end());
    binarySearch(0, times.back() * n, n, times);
    answer = tmp;
    cout << answer << endl;
    return answer;
}


int main(void) {
    // solution(6, {7, 10});
    solution(100, {2, 5});
    return 0;
}