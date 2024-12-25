def calculate_structure_sum(*args):
    sum = 0
    for element in args:
        if isinstance(element, str):
            sum += len(element)
        elif isinstance(element, int) or isinstance(element, float) or isinstance(element, bool):
            sum += element
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            sum += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            sum += calculate_structure_sum(*tuple(element.items()))
    return sum
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)