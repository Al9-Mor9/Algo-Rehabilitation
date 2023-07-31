import sys
sys.stdin = open('input.txt', 'r')


## not done

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# q = []


def dfs(x, y, c, t):
    if c == 4:
        global ans
        # w = ans
        ans = max(t, ans)
        # if w != ans:
        #     print(q, t)
        return
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = 1
            # q.append([nx, ny])
            dfs(nx, ny, c+1, t+arr[nx][ny])
            # q.pop()
            visited[nx][ny] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        cnt, temp = 0, 0
        # visited[i][j] = 1
        print(i, j)
        # q.append([i, j])
        dfs(i, j, cnt, temp)
        # q.pop()
print(ans)