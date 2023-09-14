N, K = map(int, input().split())
numbers = list(map(int, input().split()))

tmp = sum(numbers[:K])
answer = tmp
for i in range(K, N):
    tmp += numbers[i] - numbers[i-K]
    answer = max(tmp, answer)

print(answer)