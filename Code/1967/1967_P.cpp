#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, s, e, d, dist[10001];
bool dia = false;
priority_queue<pair<int, int>> pq;
vector<vector<pair<int,int>>> con;
vector<int> nominee;

int treedia(int a) {
	int max = 0;
	int result = 0;
	for (int i = 0; i <= N; i++) dist[i] = -1;
	dist[a] = 0;
	pq.push({ 0,a });

	while (!pq.empty()) {
		int here = pq.top().second;
		int distance = pq.top().first;

		pq.pop();

		for (auto it : con[here]) {
			int next = it.first;
			int ndist = it.second + distance;
			if (dist[next] != -1) continue;
			dist[next] = ndist;
			pq.push({ ndist,next });
		}
	}
	for (int i = 1; i <= N; i++) if (dist[i] > max) {
		result = i; max = dist[i];
	}
	if (!dia) {
		dia = true;  return result;
	}
	else {
		return max;
	}
}


int main() {
	scanf("%d", &N);
	con.resize(N + 1);
	for (int i = 0; i < N-1; i++) {
		scanf("%d%d%d", &s, &e, &d);
		con[s].push_back({ e,d });
		con[e].push_back({ s,d });
	}
	printf("%d", treedia(treedia(1)));
