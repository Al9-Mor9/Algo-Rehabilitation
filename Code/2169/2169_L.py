import sys
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
n, m = map(int, input().split())
mars = [list(map(int, input().strip().split())) for _ in range(n)]

for j in range(1, m) :
    mars[0][j] += mars[0][j - 1]
        
for i in range(1, n) :   
    l = [mars[i][j] + mars[i - 1][j] for j in range(m)]
    r = [mars[i][j] + mars[i - 1][j] for j in range(m)]
    
    for j in range(1, m) : l[j] = max(l[j], l[j - 1] + mars[i][j]) 
    for j in range(m-2, -1, -1) : r[j] = max(r[j], r[j + 1] + mars[i][j])    
    for j in range(m) : mars[i][j] = max(l[j], r[j])

print(mars[-1][-1])