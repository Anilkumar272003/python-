def staircase(n):
    if n <= 1:
        return n
    return staircase(n-1) + staircase(n-2)

def countWays(s):
    return staircase(s + 1)
s = int(input("Enter a number: "))
print ("Number of ways = ",)
print (countWays(s))                                                                                                                                                                                                                                                                                                          
 
