# 선수과목(Prerequisite)
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
inDegree = [1] * (V+1)

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, V+1):
    for b in graph[i]:
        inDegree[b] = max(inDegree[b], inDegree[i]+1)

print(*inDegree[1:])

# from collections import deque

# def topologySort():
#     q = deque()

#     for i in range(1, V+1):
#         if inDegree[i] == 0:
#             q.append(i)
#             result[i-1] = 1
    
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             inDegree[i] -= 1

#             ----------------------------------
#             q.append(i)
#             result[i-1] = result[now-1] + 1
#             ----------------------------------

#             ----------------------------------
#             if not inDegree[i]:
#                 q.append(i)
#                 result[i-1] = result[now-1] + 1
#             ----------------------------------


# V, E = map(int, input().split())
# graph = [[] for _ in range(V+1)]
# inDegree = [0] * (V+1)
# result = [0] * V

# for _ in range(E):
#     # a에서 b로 연결
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     inDegree[b] += 1

# topologySort()
# print(*result)
