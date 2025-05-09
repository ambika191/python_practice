
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Bitwise AND
print(f"a & b (Bitwise AND): {a & b}")

# Bitwise OR
print(f"a | b (Bitwise OR): {a | b}")

# Bitwise XOR
print(f"a ^ b (Bitwise XOR): {a ^ b}")

# Bitwise NOT
print(f"~a (Bitwise NOT of a): {~a}")
print(f"~b (Bitwise NOT of b): {~b}")

# Bitwise left shift
shift = int(input("Enter the number of positions to left shift: "))
print(f"a << {shift} (Left shift): {a << shift}")
print(f"b << {shift} (Left shift): {b << shift}")

# Bitwise right shift
print(f"a >> {shift} (Right shift):{a >> shift}")
print(f"b >> {shift} (Right shift):{b>>shift}")
