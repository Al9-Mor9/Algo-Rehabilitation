import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------
sys.setrecursionlimit(int(1e6 + 1))


def dfs(x):

    visit[x] = 1
    team.append(x) 
    num = arr[x]
    
    if not visit[num]:
        dfs(num)
    elif num in team:
        global team_lst
        idx = team.index(num)
        team_lst += team[idx:]
    else:
        return

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0 for _ in range(n + 1)]
    team_lst = []

    for _ in range(1, n + 1):
        if not visit[_]:
            team = []
            dfs(_) 
            
    print(n - len(team_lst))