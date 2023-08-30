import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# --------------------------------------
# 1 ~ 1,000
# 0 ~ 500,000
# A < B < N
# A가 선수 과목이다.
from collections import deque

n, m = map(int, input().split())
graph =[[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)] 

for _ in range(m):        
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque() 
for i in range(1, n + 1): 
    if not in_degree[i]: 
        q.append([i, 1]) 
        ans[i] = 1 

# 재수가 없으면 1000학기를 다녀야 할 수도 있다. 500학년은 교수도 피하겠다..
while q: 
    course, semester = q.popleft() 
    for nxt in graph[course]:
        in_degree[nxt] -= 1
        if not in_degree[nxt]:
            q.append([nxt, semester + 1])
            ans[nxt] = semester + 1
print(*ans[1:])




