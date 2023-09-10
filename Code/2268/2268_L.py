import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------

n, m = map(int, input().split())
tree = [0 for _ in range(int(2e7) + 1)]

def Modify(node, s, e, idx, k) :

    if idx < s or idx > e: return

    if s==e:
        tree[node]=k
        return
    
    mid = (s + e) // 2
    Modify(node * 2 , s, mid, idx, k)
    Modify(node * 2 + 1 , mid + 1, e, idx, k)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def Sum(node, s, e, l, r):

    if l > e or r < s: return 0
    if l <= s and r >= e: return tree[node]

    mid = (s + e) // 2
    val = Sum(node * 2, s, mid, l, r) + Sum(node * 2 + 1 , mid + 1, e, l, r)

    return val


for _ in range(m):
    q, a, b = map(int,input().split())

    if not q:
        if a > b: a, b = b, a
        print( Sum(1 , 0 , n - 1, a - 1 , b - 1) )
    else:
        Modify(1, 0, n - 1, a - 1, b)