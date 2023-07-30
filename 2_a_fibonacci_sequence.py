# Fibonacci Sequence
def fn(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fn(n - 1) + fn(n - 2)

def main() -> None:
    num: int = int(input("Enter a number: "))
    if num > 0:
        print(f"fn({num}) = {fn(num)}")
    else:
        print("Error in input")

if __name__ == '__main__':
    main()
