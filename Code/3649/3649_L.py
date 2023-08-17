def findBlock():
    x = int(input()) * 1e7
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    l, r = 0, n-1
    while l < r:
        l_b, r_b = arr[l], arr[r]
        candidate = l_b + r_b

        if candidate == x:
            return(f"yes {l_b} {r_b}")
        
        if candidate > x:
            r -= 1
        else:
            l += 1
    return "danger"

while True:
    try:
        print(findBlock())
    except:
        break

