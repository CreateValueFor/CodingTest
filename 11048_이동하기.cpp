#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int N, M;
	int arr[1001][1001] = { 0, };
	int arr2[1001][1001];

	cin >> N >> M;
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= M; j++)
			cin >> arr[i][j];
	for (int i=1; i<=N; i++)
		for (int j = 1; j <= M; j++) {
			int tmp = 0;
			tmp = max(arr2[i - 1][j - 1], max(arr2[i - 1][j], arr2[i][j - 1]));
			arr2[i][j] = tmp + arr[i][j];
		}
	cout << arr2[N][M] << endl;

	return 0;
}