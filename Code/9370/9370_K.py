# 미확인 도착지

from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

INF = 1e9
T = int(input())
for _ in range(T):
    V, E, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[INF] * V for _ in range(V)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        print(c, graph[a-1][b-1])
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c

    candidate = []
    for _ in range(t):
        candidate.append(int(input()))

    pprint(graph)
    pprint(candidate)