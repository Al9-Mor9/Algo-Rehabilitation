#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int A, B, C;
bool poured[201][201][201];
queue<tuple<int, int, int>> tupQue;
priority_queue<int, vector<int>, greater<>> ans;

int main(){
    scanf("%d%d%d", &A, &B, &C);
    int cap[3] = {A, B, C};
    tupQue.push({0, 0, C});
    poured[0][0][C] = true;

    while (!tupQue.empty()){
        tuple<int, int, int> front = tupQue.front();
        tupQue.pop();
        
        int a = get<0>(front);
        int b = get<1>(front);
        int c = get<2>(front);

        int cur[3] = {a, b, c};
        if (a == 0) ans.push(c);

        for (int from = 0; from < 3; from++){
            for (int to = 0; to < 3; to++){
                if (from == to) continue;
                if (cur[from] + cur[to] > cap[to]) {
                    int next[3] = {a, b, c};
                    next[from] = cur[from] - (cap[to] - cur[to]);
                    next[to] = cap[to];
                    if (poured[next[0]][next[1]][next[2]]) continue;
                    tupQue.push({next[0], next[1], next[2]});
                    poured[next[0]][next[1]][next[2]] = true;
                }
                else {
                    int next[3] = {a, b, c};
                    next[from] = 0; 
                    next[to] = cur[to] + cur[from]; 
                    if (poured[next[0]][next[1]][next[2]]) continue;
                    tupQue.push({next[0], next[1], next[2]});
                    poured[next[0]][next[1]][next[2]] = true;
                }
            }
        } 
    }

    while (!ans.empty()){
        printf("%d ", ans.top());
        ans.pop();
    }

}
