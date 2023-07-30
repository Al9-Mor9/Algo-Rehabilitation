import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 

# 5가지 테트리스 블럭이 있다

# 00  0000  000   00  000
# 00        0    00    0
# 

# 다 하려다가 접고 dfs 찾음. 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans, tmp = 0, 0
visited = [[0 for _ in range(m)] for _ in range(n)]
ans = 0

dr = [(0, -1),
      (0, 1),
      (1, 0),
      (-1, 0)]

def dfs(cur_r, cur_c, cnt, tmp):
    if cnt == 4:
        global ans
        ans = max(ans, tmp)
        return
    for dx, dy in dr:
        nxt_r, nxt_c = cur_r + dx, cur_c + dy    
        if  0 <= nxt_r < n and \
            0 <= nxt_c < m and \
            not visited[nxt_r][nxt_c]:
                visited[nxt_r][nxt_c] = 1
                dfs(nxt_r, nxt_c, cnt + 1, tmp + arr[nxt_r][nxt_c])
                visited[nxt_r][nxt_c] = 0

for i in range(n):
    for j in range(m):
        dfs(i, j, 0, 0)


for i in range(n-1):
     for j in range(m-2):
          ans = max(ans, sum(arr[i][j:j+3])+ arr[i+1][j+1])
          ans = max(ans, sum(arr[i+1][j:j+3])+ arr[i][j+1])
          
for i in range(n-2):
     for j in range(m-1):
          ans = max(ans, arr[i][j] + arr[i+1][j] + \
                         arr[i+2][j]+ arr[i+1][j+1])
          ans = max(ans, arr[i][j+1] + arr[i+1][j] + \
                         arr[i+2][j+1]+ arr[i+1][j+1])

print(ans)