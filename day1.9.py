def cruise (T,L,E):
    maxguests=0
    guests=0
    for i in range(T):
        guests+=E[i]-L[i]
        maxguests=max(maxguests,guests)

    return maxguests

T=5
E=[7,0,5,1,3]
L=[1,2,1,3,4]
print(cruise(T,L,E))
