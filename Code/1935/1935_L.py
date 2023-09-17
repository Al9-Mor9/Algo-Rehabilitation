import sys 
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#--------------------------------------

n = int(input())
arr = list(input().rstrip())
nums = [int(input()) for _ in range(n)]
stk = []
for i in arr:
    if i not in '*-+/':
        stk.append(nums[ord(i) - 65]) 
    else:
        num2 = stk.pop()
        num1 = stk.pop()

        if i == '*':    res = num1 * num2
        elif i == '-':  res = num1 - num2
        elif i == '+':  res = num1 + num2            
        elif i == '/':  res = num1 / num2

        stk.append(res)
        
print('{:.2f}'.format(stk[0]))

