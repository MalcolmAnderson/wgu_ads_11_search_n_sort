def find(lst, item, low, high, indent):
    """
    Finds index of string in list of strings, else -1.
    Searches only the index range low to high
    Note: Upper/Lower case characters matter
    """
    indent_increase = '   '
    print(indent, 'find() range', low, high)
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]:  # Base case 1: Found at mid
        print(indent, 'Found person.')
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        print(indent, 'Person not found.')
        pos = -1
    else:  # Recursive search: Search lower or upper half
        new_indent = indent + indent_increase
        if item < lst[mid]:  # Search lower half
            print(indent, 'Searching lower half.')
            pos = find(lst, item, low, mid, new_indent)
        else:  # Search upper half
            print(indent, 'Searching upper half.')
            pos = find(lst, item, mid + 1, high, new_indent)

    print(indent, 'Returning pos = %d.' % pos)
    return pos


attendees = []

attendees.append('Adams, Mary')
attendees.append('Carver, Michael')
attendees.append('Domer, Hugo')
attendees.append('Fredericks, Carlo')
attendees.append('Li, Jie')

name = input("Enter person's name: Last, First: ")
pos = find(attendees, name, 0, len(attendees)-1, '   ')

if pos >= 0:
    print('Found at position %d.' % pos)
else:
    print('Not found.')
