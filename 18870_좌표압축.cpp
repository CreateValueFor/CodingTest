#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {

	int N;
	cin >> N;
	vector<int> v, v2;
	
	int tmp;
	for (int i = 0; i < N; i++) {
		cin >> tmp;
		v.push_back(tmp);
		v2.push_back(tmp);
	}
	sort(v2.begin(), v2.end());
	v2.erase(unique(v2.begin(), v2.end()), v2.end());
	
	for (int i = 0; i < N; i++) {
		auto it = lower_bound(v2.begin(), v2.end(), v[i]);
		cout << it - v2.begin() << ' ';

	}


	return 0;
}