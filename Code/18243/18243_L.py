import sys 
input = sys.stdin.readline 
#-------------------------------------------------------

INF = 101
n, kk = map(int, input().split())
arr = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(kk):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1


for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
                

is_small = True
for i in arr:
    for j in i:
        if j > 6:
            is_small = False

print("Small World!" if is_small else "Big World!")