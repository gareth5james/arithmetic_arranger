def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5: 
        return 'Error: Too many problems.'
    
    numbers = []
    operators = []

    for p in problems:
        list = p.split()

        numbers.append(list[0])
        operators.append(list[1])
        numbers.append(list[2])

    for n in numbers:
        if not n.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(n) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    for o in operators:
        if o not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
    
    dashes = ''
    top = ''
    bottom = ''
    solutions = ''

    for i in range(0, len(numbers), 2):    
        first = numbers[i]
        second = numbers[i + 1]
        operator = operators[i // 2]
        solution = 0
        if operator == '+':
            solution = int(first) + int(second)
        elif operator == '-':
            solution = int(first) - int(second)
        
        formatLength = max(len(first), len(second)) + 2
        dashes += '-' * formatLength
        top += first.rjust(formatLength)
        bottom += operator + second.rjust(formatLength - 1)
        solutions += str(solution).rjust(formatLength)

        if i != len(numbers) - 2:
            dashes += ' '  * 4
            top += ' ' * 4
            bottom += ' ' * 4
            solutions += ' ' * 4
    
    if show_answers:
        return f'{top}\n{bottom}\n{dashes}\n{solutions}'

    return f'{top}\n{bottom}\n{dashes}'

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')