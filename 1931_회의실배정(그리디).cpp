#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> P;
vector<P> v;

bool comp(P a, P b) {
	if (a.second == b.second) {
		return a.first < b.first;
	}
	else {
		return a.second < b.second;
	}
}

int main(void) {

	int N;
	cin >> N;

	int tmp1, tmp2;
	for (int i = 0; i < N; i++) {
		cin >> tmp1 >> tmp2;
		v.push_back(make_pair(tmp1, tmp2));
	}
	
	sort(v.begin(), v.end(),comp);
	int count=1;
	int start = v[0].second;

	for (int i = 1; i < N; i++) {
		if (v[i].first >= start) {
			start = v[i].second;
			count++;
		}
	
	}
	cout << count;


	return 0;
}