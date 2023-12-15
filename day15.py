from collections import defaultdict
with open("inputs/15.txt", "r") as File:
    line = File.readline()[:-1]

def HASH(s):
    val = 0
    for char in s:
        val += ord(char)
        val *= 17
        val %= 256
    return val

steps = line.split(',')
ans_p1 = sum([HASH(step) for step in steps])

print(f"Part 1 answer: {ans_p1}")

boxes = defaultdict(list)
label_lens = defaultdict(int)

for step in steps:
    index_op = max(step.rfind('-'), step.rfind('='))
    label = step[:index_op]
    op = step[index_op]
    box = HASH(label)
    if op == '-':
        if label in boxes[box]:
            boxes[box].remove(label)
        continue
    lens = int(step[-1])
    if label not in boxes[box]:
        boxes[box].append(label)
    label_lens[label] = lens

ans_p2 = 0
for box in boxes:
    for i, label in enumerate(boxes[box]):
        ans_p2 += (box+1) * (i+1) * label_lens[label]
    
print(f"Part 2 answer: {ans_p2}")


