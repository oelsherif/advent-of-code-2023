from copy import deepcopy
from math import prod

with open("inputs/19.txt", "r") as File:
    lines = [line[:-1] for line in File]

def count_combs(combs) -> int:
    return prod([count2 - count1 + 1 for count1, count2 in combs.values()])

def count_accepted(comb, dest) -> int:
    if dest == 'A':
        return count_combs(comb)
    if dest == 'R':
        return 0
    workflow = workflows[dest]
    ans = 0
    for cond, dest in workflow:
        if not cond:
            ans += count_accepted(comb, dest)
            break
        cat = cond[0]
        op = cond[1]
        threshold = cond[2]
        x1, x2 = comb[cat]
        if op == '>':
            if x1 > threshold:
                ans += count_accepted(comb, dest)
                break
            if x2 < threshold:
                continue
            comb_passed = deepcopy(comb)
            comb_passed[cat] = (threshold+1, x2)
            ans += count_accepted(comb_passed, dest)
            comb[cat] = (x1, threshold)
        else:
            if x2 < threshold:
                ans += count_accepted(comb, dest)
                break
            if x1 > threshold:
                continue
            comb_passed = deepcopy(comb)
            comb_passed[cat] = (x1, threshold - 1)
            ans += count_accepted(comb_passed, dest)
            comb[cat] = (threshold, x2)
    return ans

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

combs0 = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
name0 = 'in'
ans_p2 = count_accepted(combs0, name0)
print(f"Part 2 answer: {ans_p2}")
