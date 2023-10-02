#include <iostream>
using namespace std;

const int MAX_K = 100; 
int N, M, L, K, x, y;
pair<int, int> comet[MAX_K];

int main(){
	scanf("%d%d%d%d", &N, &M, &L, &K);

	for (int i = 0; i < K; i++){
		scanf("%d%d", &x, &y);
		comet[i] = {x, y};
	}

	int ans = 0;
	for (int i = 0 ; i < K; i++){
		for (int j = 0; j < K; j++){
			int cnt = 0;
			int startX = comet[i].first;
			int startY = comet[j].second;

			for (int k = 0; k < K; k++){
				int curX = comet[k].first;
				int curY = comet[k].second;

				if (curX < startX) continue;
				if (curX > startX + L) continue;

				if (curY < startY) continue;
				if (curY > startY + L) continue;

				cnt++;
			}
			ans = max(ans, cnt); 
		}
	}
	printf("%d", K - ans);
}
