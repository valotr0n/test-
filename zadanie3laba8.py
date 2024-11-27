def Akkerman(m,n):
    if m == 0:
        return n + 1 
    if m > 0 and n == 0:
        return Akkerman(m-1,1)
    if m > 0 and n > 0:
        return Akkerman(m-1, Akkerman(m,n-1))
    
print(Akkerman(0,3))