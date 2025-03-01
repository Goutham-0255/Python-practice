def gcd(a,b):
    if a == 0 and b == 0:
        return 'undefined'
    
    while b:
        a,b = b,a % b
    return abs(a)



def Lcm(a,b):

    # euclidean algorithm to find lcm
    return abs(a*b)//gcd(a,b)


print(Lcm(4,5))