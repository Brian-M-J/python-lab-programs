# Palindrome
def main() -> None:
    str_val: str = input("Enter a value: ")
    if str_val == reversed(str_val):
        print("Palindrome")
    else:
        print("Not Palindrome")

    for digit in sorted(set(str_val)):
        print(f"{digit} appears {str_val.count(digit)} times")

if __name__ == "__main__":
    main()
