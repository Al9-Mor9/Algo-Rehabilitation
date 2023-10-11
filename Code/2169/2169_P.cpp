#include <iostream>
using namespace std;

const int LEFT = 1;
const int RIGHT = 2;
const int DOWN = 3;
const int MIN_INF = -11111111;

int N, M;
int arr[1001][1001], dp[1001][1001][4];
int visited[1001][1001];

int max(int a, int b, int c){
	return a > b ? a > c ? a : c : b > c ? b : c;
}

int dfs(int row, int col, int dir){
	if (row > N || col > M || row < 1 || col < 1) return MIN_INF;
	if (row == N && col == M) return arr[row][col];	
	if (visited[row][col]) return MIN_INF;
	if (dp[row][col][dir] > MIN_INF) return dp[row][col][dir];

	visited[row][col] = true;

	int left = dfs(row, col - 1, LEFT);
	int right = dfs(row, col + 1, RIGHT);
	int down = dfs(row + 1, col, DOWN);

	int maxNext = max(left, right, down);

	visited[row][col] = false;
	return dp[row][col][dir] = arr[row][col] + maxNext;
}

int main(){
	scanf("%d%d", &N, &M);

	for (int i = 1; i <= N; i++){
		for (int j = 1; j <= M; j++){
			scanf("%d", &arr[i][j]);
			for (int k = 0; k < 4; k++) dp[i][j][k] = MIN_INF;
		}
	}

	printf("%d", dfs(1, 1, 0));
}
