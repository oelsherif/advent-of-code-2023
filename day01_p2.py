with open("inputs/01.txt", "r") as File:
    lines = File.readlines()

digits = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
}

ans = 0
keys = list(digits.keys())
for line in lines:
    firsts = [line.find(key) for key in keys]
    min_index = firsts.index( min( [i for i in firsts if i > -1] ) )
    num1 = digits[keys[min_index]]

    lasts = [line.rfind(key) for key in keys]
    max_index = lasts.index( max( lasts ) )
    num2 = digits[keys[max_index]]
    ans += 10 * num1 + num2
print(ans)