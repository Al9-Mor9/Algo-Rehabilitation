import sys
sys.stdin = open('input.txt', 'r')
#####
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1]
ans = 600
## dfs 로 풀어서 끝까지 갔을 때 min값 update
# directions?
def dfs(row, col, dir, fuel):
    global ans
    if row == n:
        ans = min(ans, fuel)
        return
    for i in dr:
        if i != dir and 0 <= col + i < m:
            dfs(row+1, col+i, i, fuel + arr[row][col])

for j in range(m):
    dfs(0, j, 2, 0)
print(ans)