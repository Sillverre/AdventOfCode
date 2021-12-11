f = open("input.txt", "r")

def transform_data(arg):

    all_patterns = []
    all_outputs = []

    for line in arg:
        a,b = line.split('|')
        pattern = a.strip().split(' ')
        output = b.strip().split(' ')

        all_patterns.append(pattern)
        all_outputs.append(output)

    return all_patterns, all_outputs

def count_digits(outputs):
    count = 0
    for output in outputs:
        for digit in output:
            print(digit)
            if len(digit) < 5 or len(digit) > 6:
                count += 1

    return count

def find_one(pattern):
    for digit in pattern:
        if len(digit) == 2:
            return digit

def find_four(pattern):
    for digit in pattern:
        if len(digit) == 4:
            return digit
            
def find_seven(pattern):
    for digit in pattern:
        if len(digit) == 3:
            return digit

def find_eight(pattern):
    for digit in pattern:
        if len(digit) == 7:
            return digit

def check_diff(digit1, digit2):
    diff = ""

    if len(digit1) > len(digit2):
        tmp = digit1
        digit1 = digit2
        digit2 = tmp
    for element in digit2:
        if element not in digit1:
            diff += element

    for element in digit1:
        if element not in digit2 and element not in diff:
            diff += element
    
    return diff


def get_key(pattern):
    key = [""] * 10
    key[1] = find_one(pattern)
    key[4] = find_four(pattern)
    key[7] = find_seven(pattern)
    key[8] = find_eight(pattern)

    for digit in pattern:
        if (check_diff(key[1],digit) != "" and check_diff(key[4],digit) != "" and
            check_diff(key[7],digit) != "" and check_diff(key[8],digit) != "" ):
            # 0,6,9
            if len(check_diff(key[8],digit)) == 1:
                # 6
                if len(check_diff(key[1],digit)) == 6:
                    key[6] = digit
                # 9
                elif len(check_diff(key[4],digit)) == 2:
                    key[9] = digit
                # 0
                else :
                    key[0] = digit
            # 3
            elif len(check_diff(key[1],digit)) == 3:
                key[3] = digit
            # 5,2
            else:
                if len(check_diff(key[4],digit)) == 3:
                    key[5] = digit
                else :
                    key[2] = digit

    return key

def check_digit_encryption(key, digit):
    for key_element in key:
        if check_diff(key_element, digit) == "":
            return key.index(key_element)

def decypher(key, pattern):
    decyphered = []
    for digit in pattern:
        real_value = check_digit_encryption(key, digit)
        decyphered.append(str(real_value))

    pattern_value = int("".join(decyphered))
    return pattern_value

def part1(arg):
    all_patterns, all_outputs = transform_data(arg)

    count = count_digits(all_outputs)

    return count

def part2(arg):
    all_patterns, all_outputs = transform_data(arg)

    count = 0

    for i in range(len(all_patterns)):
        key = get_key(all_patterns[i])

        pattern_value = decypher(key, all_outputs[i])

        count += pattern_value
    
    return count

## Select function here :
print(part2(f))

