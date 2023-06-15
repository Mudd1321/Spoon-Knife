def gcd(a, b):
    r = a % b

    while r != 0:
        a = b
        b = r
        r = a % b
    
    return b

def main():
    a = 12
    b = 18
    
    c = gcd(a, b)
    print("a = ", a)
    print("b = ", b)
    print("gcd = ", c)

if __name__ == "__main__":
    main()
