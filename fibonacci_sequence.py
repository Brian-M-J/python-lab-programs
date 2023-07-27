# Fibonacci Sequence
def fn(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fn(n - 1) + fn(n - 2)


num: int = int(input("Enter a number: "))
if num > 0:
    print(f"fn({num}) = {fn(num)}")
else:
    print("Error in input")
