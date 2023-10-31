import math
for _ in range(int(input())):
    index = int(input())
    i = 9
    if index <= 9: print(index)
    else:
        # where does the index fall ? 
        i = 189
        bracket_index = 9
        digits = 2
        while index > i:
            digits += 1
            bracket_index = i
            i += 9 * pow(10, digits-1) * digits
        final_index = index - (bracket_index + 1)
        number_index = final_index // digits
        number = pow(10, digits-1) + number_index     
        first_index = (bracket_index + 1) + (digits * (number_index))
        index -= first_index
        print(str(number)[index])