#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAXN = 50;
const int MAXM = 50;
const int GREEN = 3;
const int RED = 4;
const int FLOWER = 5;

int N, M, G, R, ans, in;
pair<int, int> map[MAXN][MAXM];
vector<pair<int, int>> v;
vector<pair<int, int>> vGreen;
vector<pair<int, int>> vRed;
int d[4][2] = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

int bfs(){
    queue<pair<int, int>> green, red;
    for (int i = 0; i < G; i++) {
        green.push(vGreen[i]);
    }
    for (int j = 0; j < R; j++){
        red.push(vRed[j]);
    }

    pair<int, int> tmp[50][50];
    for (int i = 0; i < N; i++) for(int j = 0; j < M; j++) tmp[i][j] = map[i][j];

    int time = 0;
    while (!(green.empty() && red.empty())){
        while (!green.empty()) {
            pair<int, int> gTop = green.front();
            int x = gTop.first, y = gTop.second;
            if (tmp[x][y].second != time) break;
            green.pop();

            if (tmp[x][y].first == GREEN){
                for (int i = 0; i < 4; i++){
                    int nx = x + d[i][0];
                    int ny = y + d[i][1];

                    if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                    if (tmp[nx][ny].first == 1 || tmp[nx][ny].first == 2) {
                        tmp[nx][ny] = {GREEN, tmp[x][y].second + 1};
                        green.push({nx, ny});
                    }
                    else if (tmp[nx][ny].first == RED && tmp[nx][ny].second == tmp[x][y].second + 1) {
                        tmp[nx][ny].first = FLOWER;
                    }
                }
            }
        }
        while (!red.empty()){
            pair<int, int> rTop = red.front();
            int x = rTop.first, y = rTop.second;
            if (tmp[x][y].second != time) break;
            red.pop();

            if (tmp[x][y].first == RED){
                for (int i = 0; i < 4; i++){
                    int nx = x + d[i][0];
                    int ny = y + d[i][1];

                    if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                    if (tmp[nx][ny].first == 1 || tmp[nx][ny].first == 2) {
                        tmp[nx][ny] = {RED, tmp[x][y].second + 1};
                        red.push({nx, ny});
                    }
                    else if (tmp[nx][ny].first == GREEN && tmp[nx][ny].second == tmp[x][y].second + 1) {
                        tmp[nx][ny].first = FLOWER;
                    }
                }
            }
        }
        time++;
    }
    int ret = 0;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            if (tmp[i][j].first == FLOWER) ret++;
        }
    }
    return ret;
}

void recu(int red, int green, int idx){
    if (red == R && green == G) {
        ans = max(ans, bfs());
        return;
    }
    if (red > R || green > G) return;
    if (idx == v.size()) return;

    pair<int, int> coord = v[idx];
    map[coord.first][coord.second].first = GREEN;
    vGreen.push_back(coord);
    recu(red, green + 1, idx + 1);
    vGreen.pop_back();

    vRed.push_back(coord);
    map[coord.first][coord.second].first = RED;
    recu(red + 1, green, idx + 1);
    vRed.pop_back();
    
    map[coord.first][coord.second].first = 2;
    recu(red, green, idx + 1);
}

int main(){
    scanf("%d%d%d%d", &N, &M, &G, &R);
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            scanf("%d", &in);
            if (in == 2) v.push_back({i, j});
            map[i][j] = {in, 0};
        }
    }
    recu(0, 0, 0);
    printf("%d", ans);
}
