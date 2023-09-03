import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------

# A ~ B 까지 C개 간격으로 도토리를 하나씩 더 넣음.
# 규칙을 K개 만듦

# n, m, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = n * m




n, k, d = map(int, input().split())
rule = [list(map(int, input().split())) for _ in range(k)]
s, e = 0, n

def Acorn(mid):
    cnt = 0
    for a, b, c in rule:
        if mid < a: continue
        cnt += (min(mid, b) - a) // c + 1
    return cnt 

while s < e:
    mid = (s + e)//2
    acorn_cnt = Acorn(mid)
    if acorn_cnt < d:
        s = mid + 1
    else:
        e = mid

print(s)
