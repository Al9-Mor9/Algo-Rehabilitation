import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#--------------------------------------

n, k = map(int, input().split()) 
arr = list(map(int, input().split())) 
tmp = 0
for _ in range(k):
    tmp += arr[_]

ans = tmp
for _ in range(n - k):
    tmp = tmp - arr[_] + arr[_ + k]
    ans = max(ans, tmp)

print(ans)
