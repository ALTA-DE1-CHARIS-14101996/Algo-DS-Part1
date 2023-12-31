def isPrime(n):
  if n < 2 :
      return False
  else:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""
    start = start + 1
    for i in range(start, start + height):
        row = []
        for j in range(width):
            while not isPrime(start):
                start += 1
            row.append(start)
            start += 1
        row_str = ""
        for idx, num in enumerate(row):
            if idx == 0:
                row_str += str(num)
            elif len(str(num)) == 1:
                row_str += "  " + str(num)
            else:
                row_str += " " + str(num)
        result += row_str + "\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """
