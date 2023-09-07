# 텀 프로젝트

T = int(input())

for _ in range(T):
    students_num = int(input())
    students_list = [0] + list(map(int, input().split()))
    visit = [0] * (students_num + 1)
    g = 0

    for i in range(1, students_num + 1):
        if visit[i]:
            continue
            
        stack = [] + [i]
        while True:
            visit[stack[-1]] = True
            
            if visit[students_list[stack[-1]]]:
                if students_list[stack[-1]] in stack:
                    g += len(stack) - stack.index(students_list[stack[-1]])
                break
            stack.append(students_list[stack[-1]])
            
    print(students_num-g)