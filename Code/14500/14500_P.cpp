#include <iostream>
#include <stack>
using namespace std;

int N, M;
int paper[500][500];
int delta[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
bool visited[500][500];

int dfs(int x, int y, int depth, int sum);
int fuckyou(int x, int y);
stack<pair<int,int>> stk;

int main(){
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++){
		for (int j = 0; j < M; j++){
			scanf("%d", &paper[i][j]);	
		}
	}
	int ans = 0;

	for (int i = 0; i < N; i++){
		for (int j = 0; j < M; j++){
			visited[i][j] = true;
			int ret = dfs(i, j, 1, paper[i][j]);
			visited[i][j] = false;
			ans = ans > ret ? ans : ret;
			int fret = fuckyou(i, j);
			ans = ans > fret ? ans : fret;
		}
	}
	printf("%d", ans);
}

int dfs(int x, int y, int depth, int sum){
	if (depth == 4) return sum;
	int ret = 0;
	for (int i = 0; i < 4; i++){
		int nx = x + delta[i][0]; 
		int ny = y + delta[i][1]; 
		if (nx < 0 || nx >= N || ny < 0 || ny >= M ) continue;
		if (visited[nx][ny]) continue;
		visited[nx][ny] = true;
		ret = max(ret, dfs(nx, ny, depth + 1, sum + paper[nx][ny]));
		visited[nx][ny] = false;
	}
	return ret;
}

int fuckyou(int x, int y){
	int count = 0, sum = paper[x][y], m = 1000;

	for (int i = 0; i < 4; i++) {//안 쓰일 거 하나만 정하기
		int nx = x + delta[i][0]; 
		int ny = y + delta[i][1]; 
		if (nx < 0 || nx >= N || ny < 0 || ny >= M ) continue;
		count++;
		sum += paper[nx][ny];
		m = min(m, paper[nx][ny]);
	}

	if (count < 3) return 0;
	if (count == 3) return sum; 
	return sum - m;
}
