s = input() 
ans = True 
while len(s) != 1: 
    h_idx = len(s)//2
    is_odd = len(s)%2
    left, right = s[:h_idx], s[h_idx + 1:] if is_odd else s[h_idx:]
    if left != right or s != s[::-1]: ans = False 
    s = left    

print("AKARAKA" if ans else "IPSELENTI")