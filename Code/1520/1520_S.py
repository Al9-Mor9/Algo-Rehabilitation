def dfs(current_i, current_j):
    if dp[current_i][current_j] == -1:                                      # 아직 방문하지 않은 곳이라면 네 방향 더 높은곳으로부터 낮은곳방문시 경로수 누적
        dp[current_i][current_j] = 0                    
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            previous_i, previous_j = current_i + di, current_j + dj         # 이전좌표에 대한 계산 진행
            if arr[previous_i][previous_j] > arr[current_i][current_j]:     # 내리막길인 경우 (가능한 경우)
                dp[current_i][current_j] += dfs(previous_i, previous_j)     # 조건에 맞는 네 방향 경로수 누적
    return dp[current_i][current_j]

N, M = map(int, input().split())
arr = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

dp = [[-1] * (M + 2) for _ in range(N + 2)]                                 # dp 테이블 생성
dp[1][1] = 1

print(dfs(N, M))
