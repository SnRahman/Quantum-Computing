import math
import random

# Greatest Common Divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Main Shor function
def shor(N):
    if N % 2 == 0:
        return 2

    while True:
        a = random.randint(2, N - 2)
        g = gcd(a, N)
        if g > 1:
            return g

        # Find period r using brute-force (not quantum)
        r = None
        for i in range(1, N):
            if pow(a, i, N) == 1:
                r = i
                break

        if r is None or r % 2 != 0:
            continue

        x = pow(a, r // 2, N)
        if x == N - 1 or x == 1:
            continue

        factor1 = gcd(x + 1, N)
        factor2 = gcd(x - 1, N)

        if factor1 * factor2 == N:
            return factor1, factor2

# Try factoring 15
N = 15
factors = shor(N)
print("Factors of", N, "are:", factors)
