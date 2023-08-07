import sys
sys.stdin = open('../../../tmp/input.txt', 'r')
#####
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)  # [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
# 끝난 시간이 이른거 1순위, 시작시간이 이른거 2순위
arr = sorted(arr, key=lambda x: (x[1], x[0]))
# print(arr)  # [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]

ans = 0
end = 0
for s, e in arr:
    if s >= end:
        # print(s, e)
        ans += 1
        end = e
print(ans)
