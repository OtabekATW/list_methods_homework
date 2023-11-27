def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    s = ''
    while i < len(list1):

        s += list1[i] + ' '
        i += 1
        
    return s
print(main(['green', 'black', 'pink']))