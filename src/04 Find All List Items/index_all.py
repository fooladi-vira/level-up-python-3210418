def index_all(search_list, value):
    indices = []
    for i, item in enumerate(search_list):
        if item == value:
            indices.append([i])
        elif isinstance(item, list):
            # Recursively search for value in the sublist
            for index in index_all(item, value):
                indices.append([i] + index)
    return indices

# Test case
my_list = [[1, 2, 3], [2, 4, 6], [7,2,2, 8, [1, 2, 3]]]
value_to_find = 2
print(index_all(my_list, value_to_find))  # Output: [[0, 1], [1, 0]]
