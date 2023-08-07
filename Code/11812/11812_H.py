import sys

sys.stdin = open('../../../tmp/input.txt', 'r')


#####
#####

def find(node):
    cnt = 0
    lst = [node]
    while node != 1:
        cnt += 1
        lst.append(((node - 2) // k) + 1)
        node = ((node - 2) // k) + 1
    return lst


n, k, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    if k == 1:
        print(abs(x-y))
        continue
    lst1 = find(x)
    lst2 = find(y)
    # print(lst1, lst2)
    ans = 0
    p1, p2 = 0, 0
    l1, l2 = len(lst1), len(lst2)
    if l1 > l2:
        p1 = l1 - l2
        ans += p1
    elif l1 < l2:
        p2 = l2 - l1
        ans += p2
    # print("p1, p2 : ",p1, p2)
    while lst1[p1] != lst2[p2]:
        ans += 2
        p1 += 1
        p2 += 1
    print(ans)
