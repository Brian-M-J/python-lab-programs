# Sentence Statistics
def main() -> None:
    sentence: str = input("Enter a sentence: ")
    word_list: list[str] = sentence.split()
    print(f"This sentence has {len(word_list)} words.")
    dig_cnt = lo_cnt = up_cnt = 0

    for ch in sentence:
        if ch.isdigit():
            dig_cnt += 1
        elif ch.islower():
            lo_cnt += 1
        elif ch.isupper():
            up_cnt += 1

    print(
        f"This sentence has {dig_cnt} digits, {up_cnt} upper case letters, {lo_cnt} lower case letters."
    )

if __name__ == "__main__":
    main()
