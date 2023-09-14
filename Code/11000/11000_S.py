import heapq

lecture = int(input())
table = [list(map(int, input().split())) for _ in range(lecture)]
table.sort()

lecture_end_time = [table[0][1]]
for start, end in table[1:]:
    if lecture_end_time[0] <= start:
        heapq.heappop(lecture_end_time)
    heapq.heappush(lecture_end_time, end)
print(len(lecture_end_time))