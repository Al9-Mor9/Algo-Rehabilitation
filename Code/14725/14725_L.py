import sys
sys.stdin = open('input.txt', 'r') 
input = sys.stdin.readline 
#-------------------------------------------------------

def dfs(node, depth):
    for s in sorted(node.keys()) :
        print('--' * depth + s)
        dfs(node[s], depth + 1)

n = int(input())    
tree = {}

for _ in range(n):
    name = list(input().split())
    node = tree
    for f in name[1:]:
        if f not in node:
            node[f] = {}
        node = node[f]

dfs(tree, 0)