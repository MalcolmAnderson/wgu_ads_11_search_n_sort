def print_factorial(fact_counter, fact_value):
    output_string = ''

    if fact_counter == 0:      # Base case: 0! = 1
        output_string += '1'
    elif fact_counter == 1:    # Base case: print 1 and result
        output_string += str(fact_counter) + ' = ' + str(fact_value)
    else:                       # Recursive case
        output_string += str(fact_counter) + ' * '
        next_counter = fact_counter - 1
        next_value = next_counter * fact_value
        output_string += print_factorial(next_counter, next_value)

    return output_string


user_val = 3
print('%d! = ' % user_val, end="")
print(print_factorial(user_val, user_val))
