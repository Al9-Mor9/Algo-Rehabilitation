import sys
sys.stdin = open('../../../tmp/input.txt', 'r')
#####

n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()

st = 1
en = arr[-1] - arr[0]

ans = 0
while st <= en:
    mid = (st + en) // 2    # 기준 간격
    now = arr[0]    # 집 위치 init
    cnt = 1     # 공유기 갯수 init
    dist = arr[-1] - arr[0]  # 초깃값은 최대거리
    for i in range(1, n): # 순회
        if arr[i] - now >= mid: # 현재 위치와 떨어진 거리가 mid보다 멀면 공유기 설치
            dist = min(dist, arr[i] - now)  # 바로 붙어있는거니까 중간중간 간격 최솟값 업뎃
            cnt += 1
            now = arr[i]    # 현재위치 업뎃
    if cnt >= c:    # 공유기 다 설치했고, 더 많으면 간격 늘림
        st = mid + 1
        ans = max(ans, dist)
    else:   # 설치 못하면 간격 좁힘
        en = mid - 1
print(ans)