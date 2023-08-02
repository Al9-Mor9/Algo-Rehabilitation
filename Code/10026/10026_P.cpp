#include <iostream>
#include <queue>
using namespace std;

int N;
char color[101][100];
int rg[100][100];
int rgb[100][100];
int rgCnt, rgbCnt;
queue<pair<int, int>> rgQueue;
queue<pair<int, int>> rgbQueue;

int delta[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main(){
	scanf("%d", &N);

	for (int i = 0; i < N; i ++){
		scanf("%s", color[i]);
	}

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			//적녹색약
			if (!rg[i][j]) { 
				++rgCnt;
				rgQueue.push({i, j});
				rg[i][j] = rgCnt;
				while (!rgQueue.empty()){
					pair<int, int> front = rgQueue.front();
					int x = front.first, y = front.second;
					rgQueue.pop();
					for (int d = 0; d < 4; d++){
						int nx = x + delta[d][0];
						int ny = y + delta[d][1];
						if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
						if (rg[nx][ny]) continue;
						if (color[x][y] == 'B' && color[nx][ny] != 'B') continue;
						if (color[x][y] > 'B' && color[nx][ny] == 'B') continue;
                        rg[nx][ny] = rgCnt;
						rgQueue.push({nx, ny});
					}
				}
			}

			//색약 아님 
			if (rgb[i][j]) continue;
			++rgbCnt;
			rgbQueue.push({i, j});
            rgb[i][j] = rgbCnt;
			while (!rgbQueue.empty()){
				pair<int, int> front = rgbQueue.front();
				int x = front.first, y = front.second;
				rgbQueue.pop();
				for (int d = 0; d < 4; d++){
					int nx = x + delta[d][0];
					int ny = y + delta[d][1];
					if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
					if (rgb[nx][ny]) continue;
					if (color[x][y] != color[nx][ny]) continue;
                    rgb[nx][ny] = rgbCnt;
					rgbQueue.push({nx, ny});
				}
			}
		}
	}		

	printf("%d %d", rgbCnt, rgCnt);

}
