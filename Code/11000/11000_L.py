import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[0])

heap = [arr[0][1]]
for _ in range(1, n):
    end = heapq.heappop(heap)
    if end > arr[_][0]:
        heapq.heappush(heap, end)
    heapq.heappush(heap, arr[_][1])

print(len(heap))
