#include <iostream>
#include <deque>
#include <stack>
using namespace std;

int main(void) {
	int N;
	deque<int> dq;
	stack<int> stk;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		stk.push(tmp);
	}
	int num;
	int num_tmp;
	for (int i = 1; i <= N; i++) {
		
		num = stk.top();
		stk.pop();
		if (num == 1) {
			dq.push_front(i);
		}
		else if (num == 2) {
			num_tmp = dq.front();
			dq.pop_front();
			dq.push_front(i);
			dq.push_front(num_tmp);
		}
		else {
			dq.push_back(i);
		}

	}
	
	for (int i = 0; i < N;i++) {
		cout << dq.front() << " ";
		dq.pop_front();
	}


	return 0;
}