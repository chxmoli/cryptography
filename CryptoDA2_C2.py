import sympy

# Given encryption and decryption exponent pairs
pairs = [(10988423, 16784693), (25910155, 11514115)]

# Function to factor N using given pairs
def factor_N(pairs, N):
    factors = []
    for e, d in pairs:
        # Using Euler's theorem: d * e ≡ 1 (mod phi(N))
        # So, phi(N) = (e * d - 1) / k where k is some positive integer
        k = 1
        phi = (e * d - 1) // k
        
        # Since N = (p-1)(q-1) for RSA, and phi(N) = (p-1)(q-1)
        # We can find factors by solving the quadratic equation: x^2 - (N - phi + 1)x + N = 0
        a = 1
        b = -(N - phi + 1)
        c = N
        discriminant = b**2 - 4*a*c
        
        # Finding roots of the quadratic equation
        root1, root2 = sympy.symbols('root1 root2', real=True, solutions='positive')
        solutions = sympy.solve(a*root1**2 + b*root1 + c, root1), sympy.solve(a*root2**2 + b*root2 + c, root2)
        
        # Checking if the roots are integers and factors of N
        for solution in solutions:
            for root in solution:
                if sympy.Integer(root) and N % root == 0:
                    factors.append(root)
                    factors.append(N // root)
                    break
    return factors

# Given N value
N = 38749709

# Finding factors of N using given encryption and decryption exponent pairs
factors = factor_N(pairs, N)

# Removing duplicates and sorting the factors
factors = sorted(list(set(factors)))

print("The factors of N are:", factors)
