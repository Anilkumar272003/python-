def ispalindrome(s):
    return s==s[::-1]
s="malayalam"
p="anna"
ans=ispalindrome(p)
if ans:
    print('yes')
else:
    print('no')
