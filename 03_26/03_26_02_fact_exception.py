n = int(input("Enter the number: "))

def nfactorial(n):
    if n <= 0:
        raise Exception("please do not enter negative numbers or zero")
    elif n == 1:
        return 1
    else:
        return n * nfactorial(n-1)

try:
    result = nfactorial(n)
    print(result)
except Exception as e:
    print(e)
