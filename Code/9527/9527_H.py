import sys
sys.stdin = open('input.txt', 'r')
#####
import sys
import math

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def sum_f(x):
    if x <= 0:
        return 0

    seung = int(math.log2(x))  # 2**seung <= x <= 2**(seung+1)
    floor_2pow = 2 ** seung  # x보다 크지 않은 2의 제곱수 중 최댓값
    if floor_2pow == x:     # 제곱수라면 제곱수 까지의 1의 갯수 리턴
        return seung * x // 2 + 1   # n*(2^n)/2 + 1

    diff = x - floor_2pow   # 13의 경우 diff = 5 나옴
    return sum_f(floor_2pow) + diff + sum_f(diff)


# 2**53 < 10**16 < 2**54
# MAX = 10 000 0000 0000 0000
a, b = map(int, input().split())
print(sum_f(b) - sum_f(a-1))
