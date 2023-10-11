import sys
sys.stdin = open('input.txt', 'r')
#####
import copy
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for j in range(1, m):
    arr[0][j] += arr[0][j-1]

# for i in arr:
#     print(i)
# print()

for i in range(1, n):
    l2rTmp = copy.deepcopy(arr[i])
    r2lTmp = copy.deepcopy(arr[i])
    l2rTmp[0] += arr[i-1][0]
    r2lTmp[m-1] += arr[i-1][m-1]
    for j in range(1, m):
        l2rTmp[j] += max(arr[i-1][j], l2rTmp[j-1])
    for j in range(m-2, -1, -1):
        r2lTmp[j] += max(arr[i-1][j], r2lTmp[j+1])
    # print(l2rTmp, r2lTmp)
    for j in range(m):
        arr[i][j] = max(r2lTmp[j], l2rTmp[j])
# for k in arr:
#     print(k)
# print()
print(arr[-1][-1])