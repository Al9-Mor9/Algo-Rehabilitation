import sys
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
n, m, l, k = map(int, input().split())
cover = 0
star = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    for j in range(k):            
        tmp = 0
        for _ in range(k):
            if  star[i][0] <= star[_][0] <= star[i][0] + l and \
                star[j][1] <= star[_][1] <= star[j][1] + l:
                tmp += 1
        cover = max(cover, tmp)
print(k - cover)


