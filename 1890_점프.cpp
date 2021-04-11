#include <iostream>

using namespace std;



int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int N;
	int arr[101][101];
	long long DP[101][101] = { 0, };
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}
	DP[0][0] = 1;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (i == N - 1 && j == N - 1) {
				cout << DP[N - 1][N - 1];
				return 0;
			}
			if (DP[i][j] == 0) continue;
			if (i + arr[i][j] < N)
				DP[i + arr[i][j]][j] = DP[i][j] + DP[i + arr[i][j]][j];
			if (j + arr[i][j] < N)
				DP[i][j + arr[i][j]] = DP[i][j] + DP[i][j + arr[i][j]];
		}
	}
	return 0;
}