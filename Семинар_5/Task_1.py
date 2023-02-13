
def exponentiation(a, b):
    if b == 1:
        return a
    else:
        return a * exponentiation(a, b - 1)
print(exponentiation(3, 3))


