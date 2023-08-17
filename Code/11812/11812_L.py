import sys 
input = sys.stdin.readline 
n, k, q = map(int, input().split())

def cal_depth(node):
    if node == 1 : return 1

    depth = 0
    while node > (k**depth-1) //(k-1):
        depth += 1
    return depth

def parent(node):
    if node == 1: return 0
    
    depth = cal_depth(node)
    tmp = node - (k**(depth-1)-1) // (k-1)
    return (tmp-1) // k + 1 + (k**(depth-2)-1) // (k-1)


for _ in range(q):
    x, y = map(int, input().split())

    if k == 1: 
        print(abs(x-y))
        continue

    ans = 0
    depth_x = cal_depth(x)
    depth_y = cal_depth(y)
    
    if depth_x > depth_y:
        x, y = y, x
        depth_x, depth_y = depth_y, depth_x

    while depth_x != depth_y:
        y = parent(y)
        depth_y -= 1
        ans += 1
    
    while x != y:
        x = parent(x)
        y = parent(y)
        ans += 2

    print(ans)


