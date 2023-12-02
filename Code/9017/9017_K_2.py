# 크로스 컨트리
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    N = int(input())
    count = {}  # 팀 당 주자 수
    arr = list(map(int, input().split()))

    # 팀 별로 주자 수 세기
    for i in range(N):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1

    # 제외되는 팀 구하기
    excpt = {}  # 제외되는 팀
    for k, v in count.items():
        if v < 6:
            excpt[k] = 1

    # 점수 계산
    score = {}
    cnt = 1     # 점수
    for i in range(N):
        if arr[i] not in excpt:
            if arr[i] in score:
                if score[arr[i]][0] < 4:
                    score[arr[i]][0] += 1
                    score[arr[i]][1] += cnt
                elif score[arr[i]][0] == 4:
                    score[arr[i]][0] += 1
                    score[arr[i]][2] = cnt
            else:
                # [팀 당 주자 수, 상위 4명 점수 합, 5번째 주자 점수 ]
                score[arr[i]] = [1, cnt, 0]
            cnt += 1

    # 순위 정렬
    score = sorted(score.items(), key=lambda x: (x[1][1], x[1][2]))
    print(score[0][0])
