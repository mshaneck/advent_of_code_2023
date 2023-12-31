
def apply_rule(part, workflow):
    for rule in workflow:
        if rule[0]:
            return rule[1]
        prop = rule[1]
        cond = rule[2]
        value = rule[3]
        target_workflow = rule[4]
        if (cond == "<" and part[prop] < value) or (cond == ">" and part[prop] > value):
            return target_workflow
    print("No workflow matched.... something went wrong. abort.")
    exit()

workflows = {}
parts = []
state_workflow = True
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/19/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        if line == "":
            state_workflow = False
        elif state_workflow:
            # reading workflows
            name = line[:line.index("{")]
            rules_parts = line[line.index("{")+1:-1].split(",")
            rules = []
            for r in rules_parts:
                p = r.split(":")
                if len(p)>1:
                    condition_parts = p[0]
                    property = condition_parts[0]
                    condition = condition_parts[1]
                    target_value = int(condition_parts[2:])
                    if condition != "<" and condition != ">":
                        print("Something wrong with conditions. Abort")
                        exit()
                    target_workflow = p[1]

                    rules.append((False, property, condition, target_value, target_workflow))
                else:
                    rules.append((True, p[0]))
            workflows[name] = rules
        else:
            # reading parts
            part_parts = line[1:-1].split(",")
            part = {}
            for property in part_parts:
                (name,value) = property.split("=")
                part[name] = int(value)
            parts.append(part)

sum = 0
for part in parts:
    workflow = "in"
    result = apply_rule(part, workflows[workflow])
    while result != "A" and result != "R":
        result = apply_rule(part, workflows[result])
    if result == "A":
        # this part is accepted
        for prop in part:
            sum += part[prop]

print(sum)