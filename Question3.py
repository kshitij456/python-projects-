def fun(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fun(n-1) + fun(n-2))

for i in range(120):
    print(fun(i))

# Fibonacci Series