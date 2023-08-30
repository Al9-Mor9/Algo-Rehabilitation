import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
#

INF = 101
snake_ladder = [i for i in range(101)]
dist = [INF for _ in range(101)]
q = []

n, m = map(int, input().split())
for _ in range(n + m):
    a, b = map(int, input().split())
    snake_ladder[a] = b

heapq.heappush(q, [0, 1])
while q:
    cost, cur = heapq.heappop(q)
    for i in range(1, 7):
        nxt = snake_ladder[cur+i]
        if dist[nxt] > cost + 1:
            dist[nxt] = cost + 1
            heapq.heappush(q, [cost + 1, nxt])
        if nxt == 100: 
            print(dist[100])
            sys.exit()


