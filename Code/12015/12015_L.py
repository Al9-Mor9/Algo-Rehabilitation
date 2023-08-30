import sys
import bisect
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
#

n = int(input())
arr = list(map(int, input().split()))
lst = [arr[0]]
length = 1

for i in range(1, n):
    idx = bisect.bisect_left(lst, arr[i])
    if arr[i] > lst[-1]:
        lst.append(arr[i])
        length += 1
    else:
        lst[idx] = arr[i]

print(length)


