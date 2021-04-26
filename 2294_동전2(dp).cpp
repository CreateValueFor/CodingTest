#include <iostream>
#include <algorithm>

using namespace std;

int n, k;
int dp[10001] = { 0, };
int coin[101];

int main(void) {
	cin >> n >> k;
	for (int i = 1; i <= k;i++) dp[i] = 10001;
	for (int i = 1; i <= n; i++) {
		cin >> coin[i];
		for (int j = coin[i]; j <= k; j++)
			dp[j] = min(dp[j], dp[j - coin[i]] + 1);
	}

	dp[k] = (dp[k] == 10001) ? -1 : dp[k];
	cout << dp[k] << endl;


	return 0;
}