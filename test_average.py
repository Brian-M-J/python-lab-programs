# Test Average
m1, m2, m3 = map(int, input("Enter marks for three tests: ").split())
print(
    f"Average of best two test marks out of three tests' marks is {sum(sorted([m1, m2, m3])[1:]) / 2}"
)
