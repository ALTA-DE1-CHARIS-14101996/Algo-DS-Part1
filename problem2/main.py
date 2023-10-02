def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def primeX(x):
    count = 0
    n= 2
    while count < x:
        if isPrime(n):
            count+=1
            if count == x:
                return n
        n+=1         

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29