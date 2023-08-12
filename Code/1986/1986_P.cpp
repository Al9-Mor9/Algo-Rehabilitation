#include <iostream>
#include <vector>
using namespace std;

int n, m;
int k, p, q;
int x, y;
char board[1001][1001];
vector<pair<int, int>> queens;

int dkx[8] = {-1, 1, -1, 1, -2, 2, -2, 2};
int dky[8] = {-2, -2, 2, 2, -1, -1, 1, 1};

int dqx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
int dqy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};

int main(){
	scanf("%d%d", &n, &m);
	scanf("%d", &q);
	for (int i = 0; i < q; i++){
		scanf("%d%d", &x, &y);
		board[x][y] = 'q';
		queens.push_back({x, y});
	}
	scanf("%d", &k);
	for (int i = 0; i < k; i++){
		scanf("%d%d", &x, &y);
		board[x][y] = 'k';
		for (int d = 0; d < 8; d++){
			int nx = x + dkx[d];
			int ny = y + dky[d];
			if (nx <= 0 || nx > n || ny <= 0 || ny > m) continue;
			if (!board[nx][ny]) board[nx][ny] = 'b';
		}
	}
	scanf("%d", &p);
	for (int i = 0; i < p; i++){
		scanf("%d%d", &x, &y);
		board[x][y] = 'p';
	}
	
	for (int i = 0; i < q; i++){
		int qx = queens[i].first;
		int qy = queens[i].second;
		
		for (int j = 0; j < 8; j++){
			int curx = qx;
			int cury = qy;
			
			while (true){
				curx += dqx[j];
			    cury += dqy[j];	
				if (curx > 0 && curx <= n && cury > 0 && cury <= m){ 
					if (!board[curx][cury] || board[curx][cury] == 'b'){
						board[curx][cury] = 'b';
					}
					else break;
				}
				else break;
			}
		}	
	}	
	int ans = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			//printf("%c", board[i][j] ? 'X': 'O');
			ans += (board[i][j] == 0); 
		}
		//printf("\n");
	}

	printf("%d", ans);
}
