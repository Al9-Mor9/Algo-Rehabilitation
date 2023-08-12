#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int board[100][100], area[10000];
int delta[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

queue<pair<int, int>> q;

int main(){
    int M, N, K;
    int x1, y1, x2, y2;


    scanf("%d%d%d", &M, &N, &K);
    for (int i = 0; i < K; i++){
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        for (int j = x1; j < x2; j++){
            for (int k = y1; k < y2; k++){
                board[k][j] = -1;
            }
        }
    }

    int cnt = 0;

    for (int i = 0; i < M; i++){
        for (int j = 0; j < N; j++){
            if (board[i][j]) continue;
            cnt++;
            q.push({i, j});
            board[i][j] = cnt;
            area[cnt]++;

            while (!q.empty()){
                pair<int, int> front = q.front();
                q.pop();
                for (int d = 0; d < 4; d++){
                    int nx = front.first + delta[d][0];
                    int ny = front.second+ delta[d][1];
                    if (nx < 0 || ny < 0 || nx >= M || ny >= N) continue;
                    if (board[nx][ny]) continue;
                    board[nx][ny] = cnt;
                    q.push({nx, ny});
                    area[cnt]++;
                }
            }
        }
    }

    printf("%d\n", cnt);
    sort(area, area + cnt + 1);
    for (int i = 1; i <= cnt; i++) printf("%d ", area[i]);
}
