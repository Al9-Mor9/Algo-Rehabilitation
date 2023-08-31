# ACM Craft
import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    delay = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]
    inDegree = [0] * (V+1)
    time = [0] * (V+1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    
    W = int(input())

    q = deque()
    for i in range(1, V+1):
        time[i] = delay[i]
        if not inDegree[i]:
            q.append(i)
    
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            time[nxt] = max(time[nxt], time[now] + delay[nxt])
            inDegree[nxt] -= 1
            if not inDegree[nxt]:
                q.append(nxt)

    print(time[W])