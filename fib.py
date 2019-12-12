def fib():
    fibs = [1, 2]

    for i in range(1,9):
        a=0
        b=1
        while b <= 218922995834555169026:
            print(b)
            a, b = b, a+b

        ''' 
        implement Fibonacci sequence to calculate the 
        first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2
        '''

    return fibs

def main():
    print('OUTPUT', fib())
