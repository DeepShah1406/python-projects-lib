a= input("Enter Number to get Fibonacci series")

fib_series=[0,1]

for n in range(2,a):
    fibo= fib_series[n-1] +fib_series[n-1]
    fib_series.appen(fibo)
    
print(fibo)
