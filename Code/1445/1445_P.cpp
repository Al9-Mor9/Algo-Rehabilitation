#include <iostream>
#include <queue>
using namespace std;

const int INF = 9999999;

int N, M;
char row[51];
char forest[51][51];
pair<int, int> cnt[50][50]; 
pair<int, int> startPoint, flower; 

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

queue<pair<int, int>> q;

pair<int, int> min (pair<int, int> a, pair<int, int> b){
	if (a.first == b.first) {
		if (a.second < b.second) return a;
		else return b;
	} 
	if (a.first < b.second) return a;
	return b;
}


int main(){
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++){
		scanf("%s", row);
		for (int j = 0; j < M; j++){
			if (row[j] == 'S') startPoint = {i, j};
			if (row[j] == 'F') flower = {i, j};
			forest[i][j] = row[j];
			cnt[i][j] = {INF, INF};
		}
	}

	q.push(startPoint);
	cnt[startPoint.first][startPoint.second] = {0, 0};

	while (!q.empty()){
		pair<int, int> front = q.front();
		q.pop();

		for (int i = 0; i < 4; i++){
			int nx = front.first + dx[i];
			int ny = front.second + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
			int garbage = forest[nx][ny] == 'g';
			int garbageNearBy = 0;
			if (!garbage && !(nx == flower.first && ny == flower.second)) {
				for (int j = 0; j < 4; j++) {
					int nnx = nx + dx[j];
					int nny = ny + dy[j];
					if (nnx < 0 || nny < 0 || nnx >= N || nny >= M) continue;
					if (forest[nnx][nny] == 'g') garbageNearBy = 1; 
				}
			}
			pair<int, int> nextCnt = {cnt[front.first][front.second].first + garbage, cnt[front.first][front.second].second + garbageNearBy};
			if (cnt[nx][ny] > nextCnt) {
				cnt[nx][ny ] = nextCnt;
				q.push({nx, ny});
			} 
		}
	}

	printf("%d %d", cnt[flower.first][flower.second].first, cnt[flower.first][flower.second].second);
}
