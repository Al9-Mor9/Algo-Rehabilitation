import sys
from collections import deque

# 테스트케이스 개수
T = int(input())

for _ in range(T):
    N,K = map(int,input().split())              # 건물의 개수 (노드) , 건물 순서 규칙 (간선)
    time = [0]+list(map(int,input().split()))   # 건물들의 건설 시간
    build = [[] for _ in range(N+1)]            # 건설 순서 규칙
    pre_task = [0 for _ in range(N+1)]          # 진입차수
    sum_time = [0 for _ in range(N+1)]          # 특정 건물까지 걸리는 시간
                                                # 기본 배열 정리

    for _ in range(K):                          # 건설 순서 규칙 저장
        a,b = map(int,input().split())
        build[a].append(b)
        pre_task[b] += 1                        # 해당 노드를 진행하기 위해서 필요한 선행 작업의 수

    q = deque()
    for i in range(1,N+1):                      
        if pre_task[i] == 0:
            q.append(i)                         # 진입차수가 0인 인덱스 값 큐에 넣기
            sum_time[i] = time[i]

    while q:
        a = q.popleft()
        for i in build[a]:                                          
            pre_task[i] -= 1                                        # 진입차수 줄이고
            sum_time[i] = max(sum_time[a]+time[i],sum_time[i])      # 건설 비용 갱신
            print(sum_time)
            if pre_task[i] == 0:
                q.append(i)

    ans = int(input())
    print(sum_time[ans])