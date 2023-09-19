import sys
sys.stdin = open('input.txt', 'r')
#####

n = int(input())
word = input()

num = [int(input()) for _ in range(n)]
stack = []
res = 0
for i in word:
    if i.isalpha():
        stack.append(num[ord(i)-65])
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if i == '+':
            res = n1 + n2
        elif i == '-':
            res = n2 - n1
        elif i == '*':
            res = n1 * n2
        elif i == '/':
            res = n2 / n1
        stack.append(res)
print('%.2f' %stack.pop())