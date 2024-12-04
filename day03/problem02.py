import re 

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, open('input.txt').read())

def multiply(string):
    if string == '':
        return 0
    string = string[3:]
    string = string.split(',')
    if len(string) != 2:
        return 0
    string[0] = string[0][1:]
    string[1] = string[1][:-1]
    x = int(string[0]) * int(string[1])
    return x


flag = True
sum = 0
for match in matches:
    if "do" in match:
        flag = True
    if "don't" in match:
        flag = False
    if flag:
        sum += multiply(match)    
    
print(sum)
