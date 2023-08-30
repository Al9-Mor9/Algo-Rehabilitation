import sys 
input = sys.stdin.readline 
#-------------------------------------------------------
from collections import deque 


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    in_degree = [0 for _ in range(n + 1)]


    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    w = int(input())
    q = deque()
    time = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        time[i] = cost[i]
        if not in_degree[i]:
            q.append(i)
    
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            time[i] = max(time[i], time[cur] + cost[i])
            in_degree[i] -= 1
            if not in_degree[i]: 
                q.append(i)
        
    print(time[w])