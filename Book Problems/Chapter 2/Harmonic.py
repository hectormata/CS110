import sys

# Accept integer n as a command-line argument. Write to standard
# output the value of the nth harmonic number.

n = int(sys.argv[1])

total = 0.0
for i in range(1, n+1):
    # Add the ith term to the sum
    total += 1.0 / i

print(total)
