'''def factorial (n):
    if (n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

print("factorial is :",factorial(5))

def fibo(n):
    while True:
        
        if (n==0 or n==1):
            return n
        else :
           return fibo(n-1)+fibo(n-2)

res=fibo(5)
print(res)'''

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example: Print the first 10 Fibonacci numbers
result = fibonacci(10)
print(result)

