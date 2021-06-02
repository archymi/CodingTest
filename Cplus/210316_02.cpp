// https://www.acmicpc.net/problem/2580
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

#define MAX     9

int board[MAX][MAX] = {
{0, 3, 5, 4, 6, 9, 2, 7, 8},
{7, 8, 2, 1, 0, 5, 6, 0, 9},
{0, 6, 0, 2, 7, 8, 1, 3, 5},
{3, 2, 1, 0, 4, 6, 8, 9, 7},
{8, 0, 4, 9, 1, 3, 5, 0, 6},
{5, 9, 6, 8, 2, 0, 4, 1, 3},
{9, 1, 7, 6, 5, 2, 0, 8, 0},
{6, 0, 3, 7, 0, 1, 9, 5, 2},
{2, 5, 8, 3, 9, 4, 7, 6, 0}
};

bool check(int temp[MAX][MAX]) {
    vector<int> check = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    bool success = true;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            vector<int> tmp;
            tmp.push_back(temp[1 + 2*i - 1][1 + 3*j - 1]);
            tmp.push_back(temp[1 + 2*i - 1][1 + 3*j]);
            tmp.push_back(temp[1 + 2*i - 1][1 + 3*j + 1]);
            tmp.push_back(temp[1 + 2*i][1 + 3*j - 1]);
            tmp.push_back(temp[1 + 2*i][1 + 3*j]);
            tmp.push_back(temp[1 + 2*i][1 + 3*j + 1]);
            tmp.push_back(temp[1 + 2*i + 1][1 + 3*j - 1]);
            tmp.push_back(temp[1 + 2*i + 1][1 + 3*j]);
            tmp.push_back(temp[1 + 2*i + 1][1 + 3*j + 1]);
            sort(tmp.begin(), tmp.end());
            for (int k = 0; k < 9; k++) {
                if (check[k] != tmp[k]) {
                    success = false;
                    break;
                }
            }
        }
    }

    return success;
}

void input()
{
    for (int i = 0; i < MAX; i++)
    {
        for (int j = 0; j < MAX; j++)
        {
            cin >> board[i][j];
        }
    }
}

void solution() {

}

void print()
{
    for (int i = 0; i < MAX; i++)
    {
        for (int j = 0; j < MAX; j++)
        {
            cout << board[i][j] << ' ';
        }
        cout << '\n';
    }
}

int main(void) {
    // input();
    cout << check(board) << endl;
    // print();
}