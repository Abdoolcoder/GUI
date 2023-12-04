n = int(input('Enter a number'))
def factorial(n):
    if n == 0:
        number = 1
    elif n < 1:
        return 'invalid'
    else:
        number = n*factorial(n-1)
    return number

print(factorial(n))
