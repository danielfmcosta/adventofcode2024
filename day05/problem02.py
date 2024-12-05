def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip() for l in f]
        return line

def check_update(rules, update):
    for i in range(len(update)):
        for rule in rules: 
            if update[i] in rule[0]:
                if rule[1] in update[:i]:
                    return 0
    return 1

def ordering_update(rules, update):
    swap = 0
    for i in range(len(update)):
        for rule in rules: 
            if update[i] in rule[0]:
                if rule[1] in update[:i]:
                    swap = update[i]
                    update[i] = rule[1]
                    update[update.index(rule[1])] = swap
                    if check_update(rules, update):
                        return int(update[len(update)//2])
    
    return ordering_update(rules, update)


def main():
    FILENAME = 'input.txt'
    rules = read_from_file(FILENAME)
    rules.remove('')
    updates = [x for x in rules if len(x) > 5 ]
    rules = [x.split('|') for x in rules if x not in updates]
    updates = [x.split(',') for x in updates]
    sum=0
    for update in updates:
        if not check_update(rules, update):
            sum+=ordering_update(rules, update)
    print(sum)


if __name__ == "__main__":
    main()