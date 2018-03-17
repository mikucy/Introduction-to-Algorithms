def power_number(x, n):
    if n == 1:
        return x
    else:
        if n % 2 == 0:
            return power_number(x, n/2) * power_number(x, n/2)
        else:
            return power_number(x, (n-1)/2) * power_number(x, (n-1)/2) * x


print(power_number(2, 9))
print(power_number(2, 10))
