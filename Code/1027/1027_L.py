import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0 for _ in range(1001)] for _ in range(1001)]
# dp[1][1] = 1


# for i in range(n):
#     a, b, c = arr[i]

#     if dp[a][b]:
#         point = arr[i][2]


# print(i + 1)


MAX = 100 + 1

N = int(input())
arr = []
for _ in range(N):
    strength, intelligence, point = map(int, input().split())
    arr.append(((strength, intelligence), point))

cache = [[-1] * 1001 for _ in range(1001)]
visited = [False] * MAX

def maxQuest(strength, intelligence):
    result = cache[strength][intelligence]
    if result != -1:
        return result

    point = 0
    cnt = 0
    v = []

    for i in range(N):
        if arr[i][0][0] <= strength or arr[i][0][1] <= intelligence:
            if not visited[i]:
                visited[i] = True
                v.append(i)
                point += arr[i][1]
            cnt += 1

    result = cnt

    for i in range(strength, min(1000, strength + point) + 1):
        result = max(result, maxQuest(i, min(1000, intelligence + (point - (i - strength)))))

    for i in range(len(v)):
        visited[v[i]] = False

    cache[strength][intelligence] = result
    return result

print(maxQuest(1, 1))

