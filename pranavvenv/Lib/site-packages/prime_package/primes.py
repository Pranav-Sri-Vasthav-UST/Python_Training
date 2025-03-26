def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def getHighestPrime(m, n):
    for i in range(n , m - 1, -1):
        if(checkprime(i)):
            return i
    return None

def getAllPrimes(m, n):
    count = 0
    primeNumbers = []
    for x in range(m , n + 1):
        if(checkprime(x)):
            count += 1
            primeNumbers.append(x)
    return count, primeNumbers

if __name__ == "__main__":

    # Test checkprime()
    print("10 -> ", checkprime(10))
    print("11 -> ", checkprime(11))

    # Test getHighestPrime()
    print("100, 200 -> ", getHighestPrime(100, 200))

    # Test getAllPrimes()
    print("100, 200 -> ", getAllPrimes(100, 200))