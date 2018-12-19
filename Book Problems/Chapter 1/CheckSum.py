import stdio
import sys

# Accept as a command-line argument an integer n which is the first 9
# digits of an ISBN. Compute the final digit, and write the complete
# ISBN to standard output.
#
# An ISBN is legal if it consists of 10 digits and
#    d1 + 2*d2 + 3*d3 + ... + 10*d10
# is a multiple of 11. For example, 0-201-31452-5 is legal since
#    1*5 + 2*2 + 3*5 + 4*4 + 5*1 + 6*3 + 7*1 + 8*0 + 9*2 + 10*0 = 88
# and 88 is a multiple of 11.

# Accept a command-line argument.
n = int(sys.argv[1])

# Compute the weighted sum of the digits, from right to left.
total = 0
for i in range(2, 11):
    digit = n % 10;   # rightmost digit
    total += i * digit
    n //= 10

# Write check digit; use X for 10.
stdio.write('The full ISBN number is ' + sys.argv[1])
if total % 11 == 1:
   stdio.writeln('X')
elif total % 11 == 0:
   stdio.writeln('0');
else:
   stdio.writeln(11 - (total % 11))
