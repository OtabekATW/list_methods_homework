def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    list1 = [fruits.count('apple')]

    while i < len(fruits):
        if fruits[i] == 'apple':
            list1.append(fruits.index('apple', i))
        i += 1

    return list1
print(main(["apple", "banana", "apple", "pear", "apple"]))