
total_combinations = 0
workflows = {}

def visit_node(workflow, conditions):
    global workflows
    # input is the name of the workflow - list of tuples containing conditions
    # conditions is the current conditions list
    #    (False, 's', '<', 3473, 'R'), (False, 'm', '<', 1015, 'R'), (False, 'a', '>', 519, 'A'), (True, 'A')
    
    # If leaf, just offload it and terminate the recursion
    if workflow == "R" or workflow == "A":
        return process_leaf(workflow, conditions)
    
    added_cond = None
    rule_cond = conditions[:]

    for rule in workflows[workflow]:
        if added_cond is not None:
            rule_cond.append(negate_cond(added_cond))

        if not rule[0]:
            prop = rule[1]
            comp = rule[2]
            value = rule[3]
            child = rule[4]
            added_cond = (prop, comp, value)
            visit_node(child, rule_cond+[added_cond])
        else:
            child = rule[1]
            visit_node(child, rule_cond)

def negate_cond(cond):
    (prop, comp, value) = cond
    if comp == "<":
        return (prop, ">", value-1)
    else:
        return (prop, "<", value+1)

def process_leaf(name, conditions):
    global total_combinations

    # Just ignore R nodes
    if name == "A":
        print(conditions)
        # given the list of conditions e.g. [("x", ">", 2000)]
        # merge this into a list of min and max values for each letter x, m, a, s
        limits = {"x": {"min": 0, "max": 4001}, "m": {"min": 0, "max": 4001}, "a": {"min": 0, "max": 4001}, "s": {"min": 0, "max": 4001}}
        for condition in conditions:
            prop = condition[0]
            comp = condition[1]
            value = condition[2]
            if comp == ">":
                # min limit
                if limits[prop]["min"] < value:
                    limits[prop]["min"] = value
            else:
                # max limit
                if limits[prop]["max"] > value:
                    limits[prop]["max"] = value

        #print(limits)
        combinations = 1
        for lim in limits:
            mult = limits[lim]["max"] - limits[lim]["min"]-1
            #print(mult)
            if mult < 0:
                print("We have an impossible range here.")
                mult = 0
            combinations *= mult
        #print(combinations)
        total_combinations += combinations
           
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/19/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        if line == "":
            break
        
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

""" for w in workflows:
    print(w + ": " + str(workflows[w]))
 """
# need to put the workflows in a tree format
# each workflow list should be a dictionary, with the target_workflow as the key. 
# A nodes and R nodes are leaves, can be names AcceptLeaf_x and RejectLeaf_x, where x increments for each type
# once the tree is built, traverse the tree, carrying conditions down, until they accumulate at a leaf. 
# Each leaf should have the list of conditions that make it true
# passing by a rule and going to the next one (i.e. after that branch was visited), negate the condition, and accumulate to the right
# root is the "in" workflow

visit_node("in", [])
print("Test should be ")
print("167409079868000")
print(total_combinations)
""" 
              
    (s>1350):qqz{s>2770:qs,m<1801:hdj,R}                          
        (s>1350,s>2770):qs{s>3448:A,lnx} 
            (s>1350,s>2770,s>3448):A_Leaf
            (s>1350,s>2770,s<3449):lnx{m>1548:A,A}
                (s>1350,s>2770,s<3449,m>1548):A_Leaf
                (s>1350,s>2770,s<3449,m<1549):A_Leaf                     
        (s>1350,s<2771,m<1801):hdj{m>838:A,pv}  
            (s>1350,s<2771,m<1801,m>838):A_Leaf
            (s>1350,s<2771,m<1801,m<839):pv{a>1716:R,A}
                (s>1350,s<2771,m<1801,m<839,a>1716):R_Leaf
                (s>1350,s<2771,m<1801,m<839,a<1717):A_Leaf    1350<s<2771, 0<m<839, 0<a<1717, 0<x<4001
        (s>1350,s<2771,m>1800):R_Leaf                               
in{s<1351:px,qqz}                                    
    (s<1351):px{a<2006:qkq,m>2090:A,rfg}    
        (s<1351,a<2006):qkq{x<1416:A,crn}   
            (s<1351,a<2006,x<1416):A_Leaf
            (s<1351,a<2006,x>1415):crn{x>2662:A,R}
                (s<1351,a<2006,x>1415,x>2662): A_Leaf
                (s<1351,a<2006,x>1415,x>2661): R_Leaf
        (s<1351,a>2005,m>2090):A_Leaf        
        (s<1351,a>2005,m>2089):rfg{s<537:gd,x>2440:R,A}    
            (s<1351,a>2005,m>2089,s<537):gd{a>3333:R,R}
                 (s<1351,a>2005,m>2089,s<537,a>3333):R_Leaf  
                 (s<1351,a>2005,m>2089,s<537,a<3334):R_Leaf    
            (s<1351,a>2005,m>2089,s>536,x>2440):R_Leaf    
            (s<1351,a>2005,m>2089,s>536,x<2441):A_Leaf     
                                    
        




"""