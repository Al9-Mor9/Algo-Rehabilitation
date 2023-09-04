# 도토리 숨기기
import sys
sys.stdin = open('input.txt', 'r')

def calDotori(mid):
    cnt = 0
    for start, end, step in rules:
        # 기준점(mid)가 규칙의 시작점(start)보다 작으면
        # 도토리 못 넣으므로 바로 다음 규칙
        if mid < start:
            continue
        
        end = min(mid, end)     # 기준점(mid)와 규칙의 끝점(end) 중 작은 것 기준
        cnt += (end - start) // step + 1    # 도토리 개수up
    return cnt

def binarySearch():
    left = 1
    right = N
    while left < right:
        mid = (left + right) // 2

        # 1번부터 mid까지 도토리가 몇 개 저장되어 있는지
        dotoriCnt = calDotori(mid)

        # mid까지 도토리 개수가 D보다 작음 
        if dotoriCnt < D:
            left = mid + 1  # 기준점 높임

        # mid까지 도토리 개수가 D보다 크거나 같음
        else:
            right = mid # 기준점 낮춤과 동시에 답 저장
    return right

N, K, D = map(int, input().split())
rules = []
for _ in range(K):
    a, b, c = map(int, input().split())
    rules.append((a, b, c))
print(binarySearch())