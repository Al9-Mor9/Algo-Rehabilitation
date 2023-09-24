import sys
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
sys.setrecursionlimit(int(1e6))

n = int(input())
v = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
ans = 0

pairCount = n * (n - 1) // 2

for _ in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

def dfs(cur):
    global ans
    dp[cur] = 1
    
    for i in v[cur]:
        if not dp[i]:
            dp[cur] += dfs(i)

    tmp = (n - dp[cur]) * (n - dp[cur] - 1) // 2
    ans += pairCount - tmp
    return dp[cur]

dfs(1)
print(ans - pairCount)

