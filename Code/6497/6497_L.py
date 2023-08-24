import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
#
while True:
    n, m = map(int, input().split())
    if not n and not m : sys.exit()

    ans = 0
    adj_lst = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj_lst[a].append([b, c])
        adj_lst[b].append([a, c])
        ans += c

    q = []
    heapq.heappush(q, (0, 0))
    visited = [0 for _ in range(n)] 
    while q:
        cost, cur = heapq.heappop(q)
        if visited[cur]: continue
        ans -= cost
        visited[cur] = 1

        for nxt, nxt_cost in adj_lst[cur]:
            if not visited[nxt]:
                heapq.heappush(q, (nxt_cost, nxt))


    print(ans)
    




