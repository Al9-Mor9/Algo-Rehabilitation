# 냅색문제(진행중)
import sys
sys.stdin = open('input.txt', 'r')

from bisect import bisect_right
from itertools import combinations

# weight 리스트를 절반으로 나누고 
# 각각 모든 부분집합의 합을 구함

N, C = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

w_pre = weight[:N // 2]
w_post = weight[N // 2:]
sum_pre = []
sum_post = []
arr = []

for i in range(len(w_pre)+1):
    sum_pre += list(combinations(w_pre, i))

for i in range(len(w_post)+1):
    sum_post += list(combinations(w_post, i))

for i in sum_pre:
    arr.append(sum(i))

# print(sum_pre)
# print(sum_post)

# for prevalue in sum_pre:
#     idx = bisect_right(sum_post, C - prevalue)
#     print(idx)