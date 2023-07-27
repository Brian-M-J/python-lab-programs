# String Similarity
str1: str = input("Enter string 1: ")
str2: str = input("Enter string 2: ")
long, short = (
    (len(str1), len(str2)) if len(str1) > len(str2) else (len(str2), len(str1))
)
match_cnt: int = 0
for str1_ch, str2_ch in zip(str1, str2):
    if str1_ch == str2_ch:
        match_cnt += 1
print(f"Similarity between two said strings: {match_cnt / long}")
