import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
import sys

n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dp=[[-1 for _ in range(1001)] for _ in range(1001)]
visit = [0 for _ in range(51)]

def rpg(STR,INT):

    if dp[STR][INT] != -1:
        return dp[STR][INT]
    
    point=0
    cnt=0
    tmp=[]

    for i in range(n):
        if arr[i][0] <= STR or arr[i][1] <= INT:
            cnt += 1
            if not visit[i]:
                visit[i] = 1
                tmp.append(i)
                point += arr[i][2]
    
    dp[STR][INT] = cnt

    for i in range(STR, min(1000, STR + point + 1)):
        nxt_Int = min(1000, INT + point - (i - STR))
        cnt = max(cnt, rpg(i, nxt_Int))

    for _ in tmp:
        visit[_] = 0
    
    dp[STR][INT] = cnt
    return cnt

print(rpg(1,1))



# n = int(input())
# quest = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0] * 1001 for _ in range(1001)]
# dp[1][1] = 1

# for i in range(1, 1001) :
#     for j in range(1, 1001) :
#         if dp[i][j] == 0 : continue
#         cnt = 2-i-j
#         for a, b, c in quest :
#             if i >= a or j >= b : 
#                 cnt += c

#         a = i + cnt
#         b = j 
#         c = i + cnt - 1000

#         if c > 0 : 
#             a -= c
#             b += c

#         if b > 1000 :
#             b = 1000

#         for _ in range(i, a + 1) : 
#             dp[a][b] = 1
#             a -= 1
#             b += 1

#             if b > 1000 :
#                 break

# ans = 0
# for i in range(1, 1001) :
#     for j in range(1, 1001) :
#         if dp[i][j] == 0 :
#             continue
        
#         cnt = 0
#         for a, b, _ in quest :
#             if i >= a or j >= b :
#                 cnt += 1

#         ans = max(ans, cnt)

# print(ans)
