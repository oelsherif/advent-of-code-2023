with open("inputs/19.txt", "r") as File:
    lines = [line[:-1] for line in File]

def rating(part) -> int:
    return sum(part.values())

def evaluate(part, condition) -> bool:
    cat = condition[0]
    op = condition[1]
    threshold = condition[2]
    if op == '>':
        if part[cat] > threshold:
            return True
        return False
    else:
        if part[cat] < threshold:
            return True
        return False


def is_accepted(part, name) -> bool:
    workflow = workflows[name]
    for cond, dest in workflow:
        if cond and not evaluate(part, cond):
            continue
        if dest == 'A':
            return True
        if dest == 'R':
            return False
        return is_accepted(part, dest)


workflows = {}
for i, line in enumerate(lines):
    if not line:
        break
    j = line.find('{')
    name = line[:j]
    rules = line[j+1:-1].split(',')
    workflow = []
    for rule in rules:
        k = rule.find(':')
        if k == -1:
            workflow.append((None, rule))
            continue
        condition = (rule[0], rule[1], int(rule[2:k]))
        workflow.append((condition, rule[k+1:]))
    workflows[name] = workflow

parts = []
for line in lines[i+1:]:
    cats = line[1:-1].split(',') # cat is category
    part = {}
    for cat in cats:
        part[cat[0]] = int(cat[2:])
    parts.append(part)

ans_p1 = 0
for part in parts:
    name0 = 'in'
    if is_accepted(part, name0):
        ans_p1 += rating(part)
    
print(f"Part 1 answer: {ans_p1}")

