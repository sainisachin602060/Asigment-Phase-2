def binary(n):
    if n==1:
        return binary(1)
    return (bin(n))

print(binary(7))