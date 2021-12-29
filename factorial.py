num = int(input("enter the number: "))

def new_factorial(num):
    fact = 1
    if num == 0 or num  == 1:
        return 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

ans = new_factorial(num)
print(f'{num} fact is {ans}')


