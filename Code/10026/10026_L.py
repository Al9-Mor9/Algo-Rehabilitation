import sys 
sys.stdin = open('input.txt', 'r') 

# 일반 사람이 구역의 수를 찾는 법 : DFS, BFS 
# 적녹 색약은 
# Red , Green을 같은 걸로 봄 

input = sys.stdin.readline 
n = int(input()) 
lst = [list(input().strip()) for _ in range(n)] 

dr = ((1, 0), (-1, 0), (0, 1), (0, -1))
def dfs_stack(flag):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                c = lst[i][j]
                stack = [(i, j, c)]
                while stack:
                    cur_i, cur_j, cur_c = stack.pop()
                    for di, dj in dr:
                        nxt_i, nxt_j = cur_i + di, cur_j + dj
                        if 0 <= nxt_i < n and \
                            0 <= nxt_j < n and \
                            not visited[nxt_i][nxt_j]:
                            nxt_c = lst[nxt_i][nxt_j]


                            if not flag:
                                if cur_c == nxt_c:
                                    stack.append((nxt_i, nxt_j, nxt_c))
                                    visited[nxt_i][nxt_j] = True
                            if flag:
                                if (cur_c != "B" and nxt_c !="B") or \
                                    (cur_c==nxt_c=="B"):
                                    stack.append((nxt_i, nxt_j, nxt_c))
                                    visited[nxt_i][nxt_j] = True

    return cnt

print(dfs_stack(0), dfs_stack(1))
