# Check valid phone number
import re

def is_phone_number(num_str: str) -> bool:
    if len(num_str) != 12:
        return False
    if num_str.count('-') != 2 or num_str[3] != '-' or num_str[7] != '-':
        return False
    for part in num_str.split('-'):
        if not part.isnumeric():
            return False
    return True

def chk_phone_number(num_str: str) -> bool:
    ph_no_pattern: re.Pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")
    if not ph_no_pattern.match(num_str):
        return False
    return True

def main() -> None:
    ph_num: str = input('Enter a phone number: ')
    print('Without using Regular Expression')
    if is_phone_number(ph_num):
        print('Valid phone number')
    else:
        print('Invalid phone number')
    print('Using Regular Expression')
    if chk_phone_number(ph_num):
        print('Valid phone number')
    else:
        print('Invalid phone number')

if __name__ == '__main__':
    main()
