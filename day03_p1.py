with open("inputs/03.txt", "r") as File:
    lines = [line[:-1] for line in File]

digits = "0123456789"
## get list of symbols
# symbols = set()
# for line in lines:
#     for char in line:
#         if char in "." + digits:
#             continue
#         symbols.add(char)
# print(symbols)

symbols = {'*', '@', '=', '$', '#', '-', '%', '+', '&', '/'}

m, n = len(lines), len(lines[0])
ans = 0
for i, line in enumerate(lines):
    j = 0
    while j < n:
        char = line[j]
        if char not in digits:
            j += 1
            continue
        k = j + 1
        while k < n:
            if line[k] in digits:
                k += 1
                continue
            break
        num = int(line[j:k])
        y_min = max(0, i-1)
        y_max = min(i+2, m)
        x_min = max(0, j - 1)
        x_max = min(k+1, n)
        symbol_exists = False
        for a in range(y_min, y_max):
            for b in range(x_min, x_max):
                if lines[a][b] in symbols:
                    symbol_exists = True
                    break
            if symbol_exists:
                break
        if symbol_exists:
            ans += num            
        j = k
        
print(ans)