# Base Conversion
def main() -> None:
    num1: int = int(input("Enter a binary number: "), base=2)
    print(f"Decimal value for {bin(num1)} is {num1}")
    num2: int = int(input("Enter an octal number: "), base=8)
    print(f"Hexadecimal value for {oct(num2)} is {hex(num2)}")

if __name__ == "__main__":
    main()
