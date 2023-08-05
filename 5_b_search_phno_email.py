# Search text file for phone numbers and emails
import re

phone_regex: re.Pattern = re.compile(r'\+\d{12}')
email_regex: re.Pattern = re.compile(r"[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}")

def main() -> None:
    with open('example.txt', 'r') as f:
        for line in f:
            matches: list[str] = phone_regex.findall(line)
            for match in matches:
                print(match)
            matches: list[str] = email_regex.findall(line)
            for match in matches:
                print(match)

if __name__ == "__main__":
    main()
