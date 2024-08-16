def reverse_bit(num):
    n, power = 0, 31
    while num > 0:
        n += (num & 1) << power
        num = num >> 1
        power -= 1

    return n


def reverse_bit_2(num):

    def reverse_byte(num):
        n, power = 0, 7
        while num > 0:
            n += (num & 1) << power
            num = num >> 1
            power -= 1
        return n

    n, power = 0, 24
    while num > 0:
        reverse = reverse_byte(num & 0xFF)
        n += reverse << power
        power -= 8
        num = num >> 8
    return n


print(reverse_bit(18))
print(reverse_bit_2(18))
print(reverse_bit(118))
print(reverse_bit_2(118))
