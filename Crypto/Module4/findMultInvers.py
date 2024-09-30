import sympy as sp

# Define the polynomial ring over GF(2)
GF2 = sp.GF(2)

# Define the variable x
x = sp.symbols('x')

# Define the irreducible polynomial P(x) for GF(2^8)
P = x**8 + x**4 + x**3 + x + 1

# Define the polynomial a(x) whose inverse we want to find
a = x**6 + x**5 + x**3 + x**2 + x

# Use the extended Euclidean algorithm to find the inverse of a modulo P
gcd, s, t = sp.gcdex(a, P, domain=GF2)

# Check if gcd is 1 (indicating that the inverse exists)
if gcd == 1:
    # The inverse of a(x) modulo P(x) is s(x)
    a_inv = sp.simplify(s % P)
    print(f"The inverse of a(x) is: {a_inv}")
else:
    print("Inverse does not exist.")
