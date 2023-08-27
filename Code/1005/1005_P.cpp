#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int T, N, K, D[1001];
int  delay[1001], x, y, indeg[1001], w;
bool adj[1001][1001];
queue<int> que;

int main(){
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &N, &K);

		for (int i = 0; i <= N; i++) {
			D[i] = delay[i] = indeg[i] = 0;
			for (int j = 0; j <= N; j++) {
				adj[i][j] = 0;
			}
		}

		for (int i = 1; i <= N; i++) scanf("%d", &delay[i]);
        
		for (int i = 1; i <= K; i++) {
			scanf("%d%d", &x, &y);
			indeg[y]++;
			adj[x][y] = 1;
		}
        
		scanf("%d", &w);

		for (int i = 1; i <= N; i++) if (!indeg[i]) que.push(i);

		while (!que.empty()) {
			int front = que.front();
			que.pop();

			D[front] += delay[front];
			
            for (int i = 1; i <= N; i++) {
				if (!adj[front][i]) continue;
				if (D[i] < D[front]) D[i] = D[front];
				indeg[i]--;
				if (!indeg[i]) que.push(i);
			}
		}

		printf("%d\n", D[w]);
	}
}
