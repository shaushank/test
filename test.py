import re

numbers = re.compile('-?\d+')

def add_num(array):
    neg_array = []
    for num in array:
        if num < 0:
            neg_array.append(num)
    if neg_array:
        raise Exception(f'negative numbers not allowed {", ".join(map(str, neg_array))}')
    else:
        x = sum(array)
        return f'Sum is {x}'

def process_input(inp):
    if not inp:
        return 'Input cannot be empty'
    
    result = list(map(int, numbers.findall(inp)))
    return add_num(result)

