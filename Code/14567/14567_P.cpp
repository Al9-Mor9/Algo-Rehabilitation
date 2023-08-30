#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, M, A, B;
vector<int> adj[1001];
int indegree[1001];
int dist[1001];
queue<int> que;

int main(){
    scanf("%d%d", &N, &M);
    for (int i = 0; i < M; i++){
        scanf("%d%d", &A, &B);
        indegree[B]++;
        adj[A].push_back(B);
    }

    for (int i = 1; i <= N; i++){
        if (!indegree[i]){
            que.push(i);
            dist[i] = 1;
        }
    }

    while (!que.empty()){
        int front = que.front();
        que.pop();

        for (int next : adj[front]){
            if (indegree[next]) {
                indegree[next]--;
                dist[next] = max(dist[front] + 1, dist[next]);
            }
            if (!indegree[next]) {
                que.push(next);
            }
        }
    }
    
    for (int i = 1; i <= N; i++) printf("%d ", dist[i]);
}
