#include <iostream>
#include <queue>
using namespace std;

int m, n, x, y, z;
int parent[200001];
priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;

int find(int a){
	if (parent[a] == a) return a;
	return parent[a] = find(parent[a]);
}

bool uni(int a, int b){
	a = find(a);
	b = find(b);

	if (a == b) return false;
	parent[a] = b;

	return true;
}

int main(){
	while (true){
		scanf("%d%d", &m, &n);

		for (int i = 0; i <= m; i++) parent[i] = i;

		if (!m && !n) break; 
		for (int i = 0; i < n; i++){
			scanf("%d%d%d", &x, &y, &z);//x -> y에 z만큼 돈이 듦
			pq.push({z, {x, y}});
		}
		//최소 스패닝 트리를 찾고 나머지는 없애면 됨
		int ans = 0;
		while (!pq.empty()){
			pair<int, pair<int, int>> top = pq.top();
			pq.pop();

			int a = top.second.first;
			int b = top.second.second;
			
			if (!uni(a, b)) ans += top.first;
		}

		printf("%d\n", ans);
	}

}
