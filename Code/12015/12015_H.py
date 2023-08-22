import sys
sys.stdin = open('input.txt', 'r')
#####
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = [1]
x = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] > x[-1]:  # 현재 값이 x 배열의 마지막 값보다 클 경우
        x.append(arr[i])  # x 배열에 현재 값을 추가해 주고
        dp.append(dp[-1] + 1)  # 증가 부분 수열의 길이를 1 증가시킨다.
    else:  # 그렇지 않을 경우
        idx = bisect_left(x, arr[i])  # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
        x[idx] = arr[i]  # x 배열의 idx 위치에 현재 값을 넣어준다.
print(dp[-1])