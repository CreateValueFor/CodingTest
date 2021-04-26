#include <iostream>
#include <queue>
using namespace std;

int main() {
    int testcase;

    cin >> testcase;

    for (int i = 0; i < testcase; i++) {
        int N, M, cnt = 0;
        queue<pair<int, int>> q;
        priority_queue<int> pq;

        cin >> N >> M;

        for (int j = 0; j < N; j++) {
            int val;
            cin >> val;
            q.push({ j, val });
            pq.push(val);
        }

        while (!q.empty()) {
            int curIdx = q.front().first;
            int curVal = q.front().second;
            q.pop();

            if (curVal == pq.top()) {
                pq.pop();
                cnt++;
                if (curIdx == M) {
                    cout << cnt << '\n';
                    break;
                }
            }
            else {
                q.push({ curIdx, curVal });
            }
        }
    }
    return 0;
}
