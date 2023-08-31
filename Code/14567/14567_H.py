import sys
sys.stdin = open('input.txt', 'r')
#####
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

ans = [1] * (n + 1)
for i in range(n):
    for connection in arr[i]:
        ans[connection] = max(ans[connection], ans[i]+1)

print(*ans[1:])