import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#--------------------------------------
def update(node, idx, s, e):
    
    if e < idx or idx < s:
        return tree[node]

    if s == idx == e:
        tree[node] = 1
        return tree[node]

    mid = (s + e) // 2
    tree[node] = update(node * 2, idx, s, mid) + update(node * 2 + 1, idx, mid + 1, e)

    return tree[node]

def query(node, s, e, l, r):
    if e < l or r < s:
        return 0

    if l <= s and r >= e:
        return tree[node]

    mid = (s + e) // 2
    return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r)

n = int(input())
arr = list(map(int, input().split()))
arr = [[arr[i], i + 1] for i in range(n)]
arr.sort(key = lambda x: x[0])

tree = [0 for _ in range(n * 4)]
ans = 0

for idx, _ in arr:
    ans += query(1, 1, n, idx, n)
    update(1, idx, 1, n)

print(ans)