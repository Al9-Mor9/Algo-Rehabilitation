#include <iostream>
using namespace std;

int M, N;
int map[500][500]{0,};
int dp[500][500]{ 0, };

int pathfinding(int x, int y) {
	int LR[4] = { 0,1,0,-1 };
	int UD[4] = { 1,0,-1,0 };
	if (x == M - 1 && y == N - 1) return 1;
	
	if (dp[x][y] == -1) dp[x][y] = 0;
	else return dp[x][y];

		for (int i = 0; i < 4; i++) {
		int nextX = x + UD[i];
		int nextY = y + LR[i];
		if (map[nextX][nextY] < map[x][y] && nextX >= 0 && nextY >= 0 && nextX < M &&nextY < N) {
			dp[x][y] += pathfinding(nextX, nextY);
		}
		}

	return dp[x][y];
}

int main() {
	scanf("%d %d", &M, &N);
  
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &map[i][j]);
			dp[i][j] = -1;
		}
	}
	dp[M - 1][N - 1] = 1;
	pathfinding(0, 0);


	printf("%d", dp[0][0]);

}
