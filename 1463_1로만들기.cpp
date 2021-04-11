#include <iostream>

using namespace std;
int N;
int arr[1000001] = { 0, };
int main(void) {
	cin >> N;
	for (int i = 2;i < N + 1; i++) {
	
		arr[i] = arr[i - 1] + 1;
		if (i % 2 == 0) {
			if (arr[i] < arr[i / 2] + 1) arr[i] = arr[i];
			else arr[i] = arr[i / 2] + 1;
		}
		if (i % 3 == 0) {
			if (arr[i] < arr[i / 3] + 1) arr[i] = arr[i];
			else arr[i] = arr[i / 3] + 1;
		}
	
	}
	cout << arr[N];

}