#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, P, Q;
vector<pair<int, int>> plan;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;//first : end time, second : seat number;
priority_queue<int, vector<int>, greater<>> seats;
int userCount[100001];

int main(){
	scanf("%d", &N);
	for (int i = 0; i < N; i++){
		scanf("%d%d", &P, &Q);
		plan.emplace_back(P, Q);
	}

	sort(plan.begin(), plan.end());

	int seatIndex = 0;

	for (int i = 0; i < N; i++){

		while (!pq.empty()){
			pair<int, int> top = pq.top();
			if (top.first < plan[i].first){//제일 빨리 끝나는 게 지금 들어갈 거보다 더 빨리 끝나면
				pq.pop();//꺼져
				seats.push(top.second);//그 자리는 이제 쓸 수 있음
			}
			else break;
		}

		if (seats.empty()){//이때까지 쓴 자리 중 빈 게 없으면
			seatIndex++;//새 자리 
			userCount[seatIndex]++;//해당 자리를 쓴 사람의 수 ++
			pq.push({plan[i].second, seatIndex});
		}
		else {
			int top = seats.top();
			seats.pop();
			pq.push({plan[i].second, top});
			userCount[top]++;
		}
	}

	printf("%d\n", seatIndex);
	for (int i = 1; i <= seatIndex; i++) printf("%d ", userCount[i]);	

}
