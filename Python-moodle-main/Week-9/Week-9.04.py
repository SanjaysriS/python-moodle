def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def christmas_discount(order_value):
    prime_digits = [2, 3, 5, 7]
    discount = 0
    for digit in str(order_value):
        if int(digit) in prime_digits:
            discount += int(digit)
    return discount

# Example usage
print(christmas_discount(578))  # Output: 12

    

print(*sorted(min_lab_students))

print(*sorted(min_average_students))



