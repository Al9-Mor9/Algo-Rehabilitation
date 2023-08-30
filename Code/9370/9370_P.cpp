#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int INF = -1;
int T, n, m, t, s, g, h, a, b, d, x;
vector<vector<pair<int, int>>> adj;
int dist[2001];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

void dij(int start){
    for (int i = 1; i <= n; i++) dist[i] = INF;
    pq.push({0, start});

    while (!pq.empty()){
        pair<int, int> top = pq.top();
        pq.pop();

        int distance = top.first;
        int vertex = top.second;

        if (dist[vertex] > -1) continue;//이미 최적
        dist[vertex] = distance;

        for (pair<int, int> next : adj[vertex]){
            int nDist = next.first + distance;
            int nVertex = next.second;

            pq.push({nDist, nVertex});
        }
    }
}

int main(){
    
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d", &n, &m, &t);
        adj.clear();
        adj.resize(n + 1);

        scanf("%d%d%d", &s, &g, &h);//출발지, 
        
        for(int j = 0; j < m; j++){//양방향 간선
            scanf("%d%d%d", &a, &b, &d);
            if ((a == g && b == h) || (a == h && b == g)) {
                adj[a].push_back({2 * d - 1, b});//갈 수 있으면 가게
                adj[b].push_back({2 * d - 1, a});
                continue;
            }
            adj[a].push_back({2 * d, b});
            adj[b].push_back({2 * d, a});
        }
        
        dij(s);

        priority_queue<int, vector<int>, greater<int>> ans; 
        
        for(int j = 0; j < t; j++){//후보지
            scanf("%d", &x);
            if (dist[x] % 2 == 1) ans.push(x);
        }

        while (!ans.empty()){
            printf("%d ", ans.top());
            ans.pop();
        }
        printf("\n"); 
    }
}
