import sys
sys.stdin = open('../../../tmp/input.txt', 'r')
#####

import sys
import heapq
input = sys.stdin.readline

inf = float('inf')
V, E = map(int, input().split())  # 노드 수, 간선 수
k = int(input())    # 시작점
edges = [[] for _ in range(V + 1)]  # [[],[],[],[],[],[]]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append([v, w])
# print(edges)    # [[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]
dist = [inf] * (V+1)
dist[k] = 0
# print(dist)   # [inf, 0, inf, inf, inf, inf]
q = []
heapq.heappush(q, [0, k])   # 처음에는 k까지 가는데 0만큼 값이 듭네다
while q:
    cost, now = heapq.heappop(q)
    if cost > dist[now]:  # Prunning
        continue
    for edge in edges[now]:
        # (dist 배열에 edge[0]으로 가는데 저장된 값)과 (현재 값 + 해당 노드로 가는데 걸리는 값) 비교
        if dist[edge[0]] > cost + edge[1]:
            dist[edge[0]] = cost + edge[1]
            # 연결된거 확인 했으니 다음 간선 있나 확인하게 q에 push
            heapq.heappush(q, [cost + edge[1], edge[0]])

for i in range(1, V + 1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])
