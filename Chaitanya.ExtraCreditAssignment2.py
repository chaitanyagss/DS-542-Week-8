facs = []

def prime_factors(num):
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            facs.append(i)
            n = n / i
        else:
            i = i + 1
        
    print(f'Prime factors of {num} are {set(facs)}')
    print(f'Largest prime factor of {num} is {max(set(facs))}')

prime_factors(600851475143)