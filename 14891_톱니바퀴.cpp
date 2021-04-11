#include <iostream>
#include <queue>
using namespace std;

int sum_check = 1;
int result = 0;
int testcase;
bool visit[4];
deque <int> dq[4];

void Gear_turn(int Gear_num, int Gear_direction) {
	if (Gear_direction == 1) {
		int temp = dq[Gear_num].back();
		dq[Gear_num].pop_back();
		dq[Gear_num].push_front(temp);
	}
	else {
		int temp = dq[Gear_num].front();
		dq[Gear_num].pop_front();
		dq[Gear_num].push_back(temp);
	}
}

void Gear_Check(int Gear_num, int Gear_direction) {
	visit[Gear_num] = true;
	int Prev_Gear_num = Gear_num - 1; int Next_Gear_num = Gear_num + 1;

	if (Prev_Gear_num >= 0 && !visit[Prev_Gear_num]) {
		if (dq[Prev_Gear_num][2] != dq[Gear_num][6])
			Gear_Check(Prev_Gear_num, (Gear_direction) * (-1));
	}

	if (Next_Gear_num < 4 && !visit[Next_Gear_num]) {
		if (dq[Next_Gear_num][6] != dq[Gear_num][2])
			Gear_Check(Next_Gear_num, (Gear_direction) * (-1));
	}
	Gear_turn(Gear_num, Gear_direction);
}


int main(){
    cin.tie(0);
    ios::sync_with_stdio(0);
    for (int i=0; i<4;i++){
        string str;
        cin >> str;
        for (int j= 0; j<8; j++){
            dq[i].push_back((str[j]-'0'));
        }
	cin >> testcase;
	while (testcase--) {
		int Gear_num, Gear_direction;
		cin >> Gear_num >> Gear_direction;

		Gear_Check(Gear_num - 1, Gear_direction);
		memset(visit, false, sizeof(visit));
	}
	
	for (int i = 0; i < 4; i++) {
		if (dq[i][0] == 1) 
			result += sum_check;
		sum_check *= 2;
	}
	cout << result;
	return 0;
}