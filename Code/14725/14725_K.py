# 개미굴
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
info = []
for _ in range(N):
    arr = list(input().split())
    info.append(arr[1:])
    info.sort()
print(info)

answer = []
for i in range(N):
    if i == 0:
        

    