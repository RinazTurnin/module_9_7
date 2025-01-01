def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        counter = 0
        for i in range(1, result + 1):
            if result % i == 0:
                counter += 1
        if counter > 2:
            print('Cоставное')
        else:
            print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
