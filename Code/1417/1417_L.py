import sys 
sys.stdin = open('input.txt', 'r') 

# 다솜이를 제외한 놈들을 줄 세워 놓고,
# 앞서부터 빼고 매수하고 다시 줄세우면 된다. 

# 매번 정렬로 풀거나,
# 힙큐(우선순위 큐)로 풀거나

input = sys.stdin.readline 
n = int(input()) 
dasom = int(input()) 
lst = [int(input()) for _ in range(n-1)]
ans = 0
if n == 1:
    print(ans)
    sys.exit()

    
# sol)1
lst.sort()
while lst[-1] >= dasom:
    dasom += 1
    lst[-1] -= 1
    ans += 1
    lst.sort()
print(ans)

# sol)2
import heapq
q = []
for i in lst:
    heapq.heappush(q, -i)
while True:
    tmp = -heapq.heappop(q)
    if dasom > tmp:
        break
    tmp -= 1
    dasom += 1
    ans += 1
    heapq.heappush(q, -tmp)

print(ans)





