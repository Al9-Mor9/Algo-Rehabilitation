import sys
sys.stdin = open('../../../tmp/input.txt', 'r')
#####
# from collections import deque


n, m = map(int, input().split())
arr = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().split())
    arr[a] = b
visited = [0] * 101
# print(arr)
q = [1]
visited[1] = 1
while q:
    now = q.pop(0)
    for i in range(1, 7):
        nxt = now + i
        if nxt > 100:
            continue

        tmp = arr[nxt]

        if not visited[tmp]:
            q.append(tmp)
            visited[tmp] = visited[now] + 1
            if tmp == 100:
                q = []
                break
        # print(visited)
print(visited[100]-1)