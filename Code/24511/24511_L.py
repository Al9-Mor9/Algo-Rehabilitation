import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#--------------------------------------
from collections import deque

n = int(input())
qstk = list(map(int, input().split())) 
arr = list(map(int, input().split())) 
m = int(input())                        
query = list(map(int, input().split())) 

q = deque([])
for i in range(n):
  if not qstk[i]:
    q.appendleft(arr[i])

if not q:
  print(*query)
  sys.exit()

for i in range(m):
  q.append(query[i])
  print(q.popleft(), end = " ")