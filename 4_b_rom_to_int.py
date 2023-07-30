# Convert roman numeral to integer
def rom_2_int(rom_str: str) -> int:
    roman_dict: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value: int = 0
    right_val: int = roman_dict[rom_str[-1]]
    for numeral in reversed(rom_str):
        left_val: int = roman_dict[numeral]
        if left_val < right_val:
            value -= left_val
        else:
            value += left_val
        right_val = left_val
    return value

def main() -> None:
    roman_str: str = input('Enter a valid roman numeral: ')
    print(f"Integer value of {roman_str} is {rom_2_int(roman_str)}")

if __name__ == '__main__':
   main()