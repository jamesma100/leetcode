def sum(a, b):
    carry = 0
    while b:
        res = a & b
        a = a ^ b
        b = res << 1
    return a

if __name__ == "__main__":
    print(sum(1, 3))