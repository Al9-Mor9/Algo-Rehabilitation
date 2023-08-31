import sys
sys.stdin = open('input.txt', 'r')
#####
from copy import deepcopy
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우 순서
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# arr에 저장된 값에 따라 바로바로 처리하기 위해 모드를 지정
mode = [
    [],
    [[0], [1], [2], [3]],   # 한쪽 방향
    [[0, 1], [2, 3]],       # ㅡ, ㅣ
    [[0, 3], [1, 3], [1, 2], [0, 2]], # ┐, └, ┌, ┘
    [[0, 1, 3], [1, 2, 3], [0, 1, 2], [0, 2, 3]],   # ├, ┬, ┤, ┴
    [[0, 1, 2, 3]]  # +
]

cctv = []
for i in range(n):
    for j in range(m):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([arr[i][j], i, j])
def dfs(indx, _arr):
    global ans
    if indx == len(cctv):   # 종료조건, cctv 갯수랑 indx랑 같으면 break
        cnt = 0
        for i in range(n):
            cnt += _arr[i].count(0)
        ans = min(ans, cnt)
        return
    _ar = deepcopy(_arr)  # 한쪽방향으로 쭉 진행 후 dfs 들어가기 위해 복사
    cctv_number, x, y = cctv[indx]
    for select in mode[cctv_number]:    # select = [0, 1], [2, 3]
        for ind in select:
            nx, ny = x, y
            dx = dr[ind][0]
            dy = dr[ind][1]
            while True:  # 가야할 방향으로 쭉 진행해봄
                nx += dx
                ny += dy
                if 0 <= nx < n and 0 <= ny < m:
                    if _ar[nx][ny] == 0:
                        _ar[nx][ny] = 7
                    elif _ar[nx][ny] == 6:
                        break
                else:
                    break
        dfs(indx + 1, _ar)  # 다음 cctv 돌려보기위해 dfs
        _ar = deepcopy(_arr) # 갔다오면 보드 초기화

# print(cctv)
ans = 64
dfs(0, arr)
print(ans)