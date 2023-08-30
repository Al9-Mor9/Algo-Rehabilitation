import sys 
sys.stdin = open("input.txt", "r")

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
        time[i] = cost[i]       # 전부 본인 건물 짓는 시간으로 초기화(최소)
        if not in_degree[i]:    
            q.append(i)
    
    while q: 
        cur = q.popleft()       # 현재 해당 노드는 최소값을 가짐
        for nxt in graph[cur]: 
            time[nxt] = max(time[nxt], time[cur] + cost[nxt]) # cur을 짓고 나서 nxt을 짓는 데 까지 걸리는시간.
            in_degree[nxt] -= 1
            if not in_degree[nxt]: 
                q.append(nxt)
        
    print(time[w])