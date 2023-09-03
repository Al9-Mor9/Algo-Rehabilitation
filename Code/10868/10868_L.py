import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------

n, m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(int(2e5))]


def init(node, s, e):
    if s == e:
        tree[node] = arr[s]
        return tree[node]
    
    mid = (s + e) // 2
    tree[node] = min(init(node*2, s, mid),
                     init(node*2 + 1, mid + 1, e))

    return tree[node]

def search(node, s, e, l, r):
    if s > r or e < l:
        return int(1e9)
    
    if l <= s and e <= r:
        return tree[node]
    
    mid = (s + e) // 2
    return min(search(node*2, s, mid, l, r),
               search(node*2 + 1, mid + 1, e, l, r))

init(1, 0, n-1)
for _ in range(m):
    a, b = map(int,input().split())
    print(search(1, 0, n - 1, a - 1, b - 1))


