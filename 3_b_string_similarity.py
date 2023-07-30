# String Similarity
def main() -> None:
    str1: str = input("Enter string 1: ")
    str2: str = input("Enter string 2: ")
    long, short = (
        (l_s1, l_s2) if (l_s1:=len(str1)) > (l_s2:=len(str2)) else (l_s2, l_s1)
    )
    match_cnt: int = 0
    for str1_ch, str2_ch in zip(str1, str2):
        if str1_ch == str2_ch:
            match_cnt += 1
    print(f"Similarity between two said strings: {match_cnt / long}")

if __name__ == '__main__':
    main()
