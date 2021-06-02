// https://programmers.co.kr/learn/courses/30/lessons/62048?language=cpp
#include <iostream>
#include <cmath>
using namespace std;

long long solution(int w,int h) {
    long long answer = 0;

    for (int i = 0; i < w; i++) {
        answer += static_cast<int>((double)h*i / w);
    }
    return answer * 2;
}

int main(void) {
    solution(8, 12);
}