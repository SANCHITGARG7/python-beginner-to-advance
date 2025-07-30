def iterativefactorial(n):
    result =1
    for i in range(n,0,-1):
        result = result*i
    return result
#print(iterativefactorial(5))
#output = 120

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) 
print(factorial(5))

