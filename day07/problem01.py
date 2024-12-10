def read_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def improve_readability(equations):
    results = []
    numbers = []
    for equation in equations:
        results.append(equation[:equation.index(':')])
        temp = equation[equation.index(':')+2:]
        numbers.append(temp.split(' ')) 
    return results, numbers

def test_operator(operator, num1, num2):
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '*':
        return int(num1) * int(num2)
    elif operator == '||':
        return int(str(num1) + str(num2))
    
def calculate_result(equation):
    result = 0
    operator = '+'
    for i in range(len(equation)):
        if equation[i] in ['+', '*']:
            operator = equation[i]
        else:
            result = test_operator(operator, result, equation[i])
    return result

def check_for_validity(result, numbers):   
    possible_results = []
    operators = ['+', '*']
    print(numbers)
    len_numbers = len(numbers)
    for i in range(pow(len(operators), len_numbers-1)):
        temp = []
        for j in range(len_numbers):
            temp.append(numbers[j])
            if j < len_numbers-1:
                temp.append(operators[i % len(operators)])
                i = i // len(operators)
        possible_results.append(temp)
    
    for possible_result in possible_results:
        if calculate_result(possible_result) == int(result):
            return int(result)
    return 0

def main():
    FILENAME = 'input.txt'
    equations = read_from_file(FILENAME)
    results, numbers = improve_readability(equations)
    sum = 0
    for i in range(len(results)):
        sum+=check_for_validity(results[i], numbers[i])
    print(sum)



if __name__ == "__main__":
    main()
