with open("inputs/01.txt", "r") as File:
    lines = File.readlines()

digits = "0123456789"
ans = 0
for line in lines:
    for char in line:
        if char in digits:
            num1 = char
            break
    for char in line[::-1]:
        if char in digits:
            num2 = char
            break
    ans += int(num1 + num2)
print(ans)