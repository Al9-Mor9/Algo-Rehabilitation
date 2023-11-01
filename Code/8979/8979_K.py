# 올림픽
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort(key = lambda x: (x[1], x[2], x[3]), reverse = True)

tmp = 0
rank = 1
for i in range(N):
    if i != 0:
        if medals[i-1][1:] == medals[i][1:]:
            tmp += 1
        else:
            if tmp:
                rank += tmp
                tmp = 0
            rank += 1
    if medals[i][0] == K:
        print(rank)
        break