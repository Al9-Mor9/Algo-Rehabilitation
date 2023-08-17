def DFS(depth):
    global cnt
    if depth == n:
        cnt += 1
        return
    
    for candidate in range(n):
        if visit[candidate]: continue
        r[depth] = candidate
        flag = True
        
        for i in range(depth):
            if r[depth] == r[i] or \
            abs(r[depth] - r[i]) == depth - i: \
            flag = False
                
        if flag:
            visit[candidate] = True
            DFS(depth + 1)
            visit[candidate] = False

n = int(input())
cnt = 0 
r = [0] * n
visit = [False] * n

DFS(0)
print(cnt)