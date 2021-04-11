#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;
int M;
int sqr;

int main() {
    cin >> M >> N;
    for (int i = M; i <= N; i++) {
        sqr = sqrt(i);
        //2,3 일경우 출력함, 정수형 출력으로 선언하여 값 보정
        if (sqr == 1 && i != 1) {
            cout << i << '\n';
            continue;
        }
        //홀수에 대하여
        if (i % 2) {
            for (int j = 2; j <= sqr; j++) {
                if (!(i % j))
                    break;
                if (j == sqr) {
                    cout << i << '\n';
                }
            }
        }
    }
}