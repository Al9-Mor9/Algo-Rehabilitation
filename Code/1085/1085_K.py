# 직사각형에서 탈출
x, y, w, h = map(int, input().split())
a = min(w-x, h-y)
b = min(x, y)
print(min(a, b))