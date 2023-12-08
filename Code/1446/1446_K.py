# 지름길
import sys
sys.stdin = open('input.txt', 'r')

import heapq

INF = int(1e9)

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))   # 거리, 현재 위치
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        # 힙큐에서 뺴낸 값이 now까지 가는 데 최소비용이 아닐 수도 있음
        if dist > distance[now]:
            continue

        for adjnode, adjcost in graph[now]:
            cost = dist + adjcost
            if cost < distance[adjnode]:
                distance[adjnode] = cost
                heapq.heappush(q, (cost, adjnode))

N, D = map(int, input().split())    # 지름길 개수, 고속도로 길이
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

# 거리 1로 초기화
for i in range(D):
    graph[i].append((i+1, 1))   # (도착지점, 거리)

# 지름길 있는 경우 업데이트
for _ in range(N):
    s, e, length = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, length))

dijkstra(0)
print(distance[D])

