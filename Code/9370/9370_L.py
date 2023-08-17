import heapq

# 각 후보지까지 최단 거리. 
# 그게 gh를 지나가는 최단 거리와 같으면 된다.
INF = int(2e6) #1000 * 2000

def dijktra(s, n, graph):
    dist = [INF for _ in range(n + 1)]

    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost: continue
        for nxt in graph[cur]:
            nxt_cost = cost + nxt[1]
            if nxt_cost < dist[nxt[0]]:
                dist[nxt[0]] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt[0]))

    return dist

def solve():
    ans = []
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    candidate = [int(input()) for _ in range(t)]
    s_to_node = dijktra(s, n, graph)
    g_to_node = dijktra(g, n, graph)
    h_to_node = dijktra(h, n, graph)

    for cand in candidate:
        if s_to_node[g] + g_to_node[h] + h_to_node[cand] == s_to_node[cand] or\
            s_to_node[h] + h_to_node[g] + g_to_node[cand] == s_to_node[cand]:
            ans.append(cand)
    ans.sort()

    print(*ans)


T = int(input())
for _ in range(T):
    solve()