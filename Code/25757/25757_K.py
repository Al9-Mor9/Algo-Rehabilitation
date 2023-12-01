# 임스와 함께하는 미니게임
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, gameType = map(str, input().split())
N = int(N)
players = set()
for i in range(N):
    player = input().rstrip()
    players.add(player)
p = len(players)

if gameType == 'Y':
    print(p)
elif gameType == 'F':
    print(p//2)
else:
    print(p//3)