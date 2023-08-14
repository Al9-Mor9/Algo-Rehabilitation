import sys
sys.stdin = open('../../../tmp/input.txt', 'r')
#####

import heapq
import sys
input = sys.stdin.readline

inf = 100000000000
# inf = float('inf') 하니까 오답 나왔다.
# 만약 s→t 로 이동이 불가능하고
# (거리 = INF), h→t 혹은 g→t의 이동도 불가능한 경우 목적지에 도착할 수 없지만,
# INF + INF = INF 가 되어 정답 처리를 하게 된다는 점을 고려해야 한다.
T = int(input())
for tc in range(1, T + 1):
    # print("####################")
    n, m, t = map(int, input().split())  # 노드, 간선, 목적지 후보
    s, g, h = map(int, input().split())  # 시작점, 교차로 양 끝(노드)
    arr = [[] for _ in range(n+1)]

    for _ in range(m):

        a, b, d = map(int, input().split())
        arr[a].append([d, b])
        arr[b].append([d, a])

    anslst = []
    for _ in range(t):
        anslst.append(int(input()))     # 목적지 후보들

    # (s에서 시작해 g, h를 거쳐 가는 최솟값)과 (s에서 바로 가는 바로가는 최소값)이 같으면 정답
    # 즉, s -> g -> h -> anslst 또는 s -> h -> g -> anslst이면 정답
    # 그럼 s, g, h 각각 다익스트라 해서 리스트를 다 갖고 있어야 한다

    def dijkstra(start):
        dist = [inf] * (n + 1)
        dist[start] = 0
        q = []
        heapq.heappush(q, [0, start])   # 시작점 초기화
        # print(dist)
        while q:
            # print(q)
            nowVal, now = heapq.heappop(q)
            # print(nowVal, now)
            for cost, nxt in arr[now]:
                # print(cost, nxt)
                if dist[nxt] > nowVal + cost:
                    dist[nxt] = nowVal + cost
                    heapq.heappush(q, [nowVal + cost, nxt])
        return dist

    s_find = dijkstra(s)
    g_find = dijkstra(g)
    h_find = dijkstra(h)

    ans = []
    for _t in anslst:
        if s_find[g] + g_find[h] + h_find[_t] == s_find[_t] or s_find[h] + h_find[g] + g_find[_t] == s_find[_t]:
            ans.append(_t)
    ans.sort()
    print(*ans)
