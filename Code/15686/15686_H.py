import sys
sys.stdin = open('../../../tmp/input.txt', 'r')
#####
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chick = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chick.append([i, j])

def find_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

res = float('inf')
# 각 치킨집들 선택한 것들에 대해
for c_lst in combinations(chick, m):  # [([0, 1], [3, 0]), ([0, 1], [4, 0]), ..., ([4, 1], [4, 4])]
    c_comb_dist = 0
    for h in house:     # 각각의 집마다
        h_shortest_dist = float('inf')
        for idx in range(m):    # 선택한 치킨집 리스트들에 대해
            # 한 집에 걸리는 치킨 거리를, 선택한 치킨집들중 최소
            h_shortest_dist = min(h_shortest_dist, find_dist(h, c_lst[idx]))
        c_comb_dist += h_shortest_dist
    res = min(res, c_comb_dist)
print(res)