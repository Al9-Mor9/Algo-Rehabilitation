import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#--------------------------------------
from collections import deque
dr = [[1, 0], [-1, 0],
      [0, 1], [0, -1]]
INF = 125 * 9 + 1
t = 0
def zelda(n):
    if not n: sys.exit()
    global t
    t += 1
    ThiefRupee = [list(map(int, input().split())) for _ in range(n)]
    arr = [[INF for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0, 0, ThiefRupee[0][0]))
    while q:
        x, y, rupee = q.popleft()

        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                tmp = rupee + ThiefRupee[nx][ny]
                if arr[nx][ny] > tmp:
                    arr[nx][ny] = tmp
                    q.append((nx, ny, tmp))                
    
    print(f'Problem {t}: {arr[n-1][n-1]}')

while True: zelda(int(input()))

