#include <iostream>
#include <vector>
using namespace std;

const int UP = 0;
const int RIGHT = 1;
const int DOWN = 2;
const int LEFT = 3;

int N, M;

int office[8][8];

vector<pair<int, int>> cctv;

bool work(int nx, int ny, int* curX, int* curY, int cpy[8][8]){
    if (nx < 0 || ny < 0 || nx >= N || ny >= M) return false;
    if (cpy[nx][ny] == 6) return false;
    if (cpy[nx][ny] == 0) cpy[nx][ny] = '#';
    *curX = nx; *curY = ny;
    return true;
}

int dfs(int idx, int curOffice[8][8]){
    if (idx == cctv.size()){
        int ret = 0;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++){
                ret += !curOffice[i][j];
            }
        }
        return ret;
    }

    pair<int, int> cur = cctv[idx];
    int tp = office[cur.first][cur.second];
    
    int ret = 9999;


    if (tp != 2) {
        if (tp > 2) tp--;
        for (int i = 0; i < 4; i++){//네 방향으로 돌려보기. 시작점
            int cpy[8][8];
            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ; j < M; j++) {
                    cpy[i][j] = curOffice[i][j];
                }
            }
            
            for (int j = 0; j < tp; j++){
                int dir = (i + j) % 4;
                int curX = cur.first;
                int curY = cur.second;
                
                if (dir == UP) {
                    while (true){
                        int nx = curX - 1; 
                        int ny = curY;
                        if (!work(nx, ny, &curX, &curY, cpy)) break;
                    } 
                }
                if (dir == DOWN) {
                    while (true){
                        int nx = curX + 1; 
                        int ny = curY;
                        if (!work(nx, ny, &curX, &curY, cpy)) break;
                    }
                }
                if (dir == LEFT) {
                    while (true){
                        int nx = curX; 
                        int ny = curY - 1;
                        if (!work(nx, ny, &curX, &curY, cpy)) break;
                    }
                }
                if (dir == RIGHT) {
                    while (true){
                        int nx = curX; 
                        int ny = curY + 1;
                        if (!work(nx, ny, &curX, &curY, cpy)) break;
                    }
                }
            }
            ret = min(ret, dfs(idx + 1, cpy));
        }
    }
    else {
        for (int i = 0; i < 2; i++){//네 방향으로 돌려보기. 시작점
            int cpy[8][8];
            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ; j < M; j++) {
                    cpy[i][j] = curOffice[i][j];
                }
            }
            
            int curX = cur.first;
            int curY = cur.second;
            
            if (i == 0) {
                while (true){
                    int nx = curX - 1; 
                    int ny = curY;
                    if (!work(nx, ny, &curX, &curY, cpy)) break;
                } 
                curX = cur.first;
                curY = cur.second;
    
                while (true){
                    int nx = curX + 1; 
                    int ny = curY;
                    if (!work(nx, ny, &curX, &curY, cpy)) break;
                }
            }
            else {
                while (true){
                    int nx = curX; 
                    int ny = curY - 1;
                    if (!work(nx, ny, &curX, &curY, cpy)) break;
                }
                curX = cur.first;
                curY = cur.second;
                while (true){
                    int nx = curX; 
                    int ny = curY + 1;
                    if (!work(nx, ny, &curX, &curY, cpy)) break;
                }
            }
        ret = min(ret, dfs(idx + 1, cpy));
        }
    }


    return ret;
}

int main(){
    scanf("%d%d", &N, &M);

    for (int i = 0; i < N; i++){
        for (int j =0; j < M; j++){
            scanf("%d", &office[i][j]);
            if (office[i][j] && office[i][j] < 6) {
                cctv.push_back({i, j});
            }
        }
    }

    int ans = dfs(0, office);

    printf("%d", ans);
}
