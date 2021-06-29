# subtracting 1 from a decimal number flips rightmost set bit and all bits after it
# n & (n-1) clears rightmost set bit, bits after it are unaffected because they're all 0's (in n)
# 10: 00001010
#  9: 00001001
# runtime: loop through number of set bits -> O(n)

def count_one(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count

# simply loop through all bits
def count_one2(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


if __name__ == "__main__":
    print(count_one(11))
    print(count_one2(11))