import sys
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
import heapq

n = int(input())

heap = []
computers = [0 for _ in range(n)]
cnt = [0 for _ in range(n)]
com = 0

for _ in range(n):
    p, q = map(int, input().split())
    heapq.heappush(heap, [p, q])

while heap:
    p, q = heapq.heappop(heap)
    for i in range(n):
        if computers[i] <= p:
            if computers[i] == 0: com += 1
            computers[i] = q
            cnt[i] += 1
            break

print(com)
for i in cnt:
    if i: print(i, end= " ")