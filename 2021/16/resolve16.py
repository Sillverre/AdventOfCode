f = open("input.txt", "r")

def transform_data(arg):
    binary_string = ""
    file = arg.readline().strip()
    for elmt in file:
        elmt_int = int(elmt, 16)
        elmt_bin = '{0:04b}'.format(elmt_int)
        binary_string += elmt_bin

    return binary_string

def read_litteral(binary_string, start):
    number = ""
    # Digit starting with 1
    while binary_string[start] == "1":
        digit_binary = binary_string[start+1:start+5]
        number += digit_binary
        start += 5

    # Last digit starting with 0
    digit_binary = binary_string[start+1:start+5]
    number += digit_binary
    start += 5
    print("Number to decode: ", number)
    return int(number,2), start

def read_operator(type_ID, binary_string, start, summVersion):
    # Get Length type ID
    length_type_ID = binary_string[start]
    start += 1
    # Get lenght
    if length_type_ID == "0":
        length = binary_string[start: start + 15]
        start += 15
        length_packets = int(length,2)
        begin = 0
        numbers = []
        while begin < length_packets:
            print("Enter Subpacket by length : ", binary_string[start:])
            number, advanced, summVersion = uncode_binary(binary_string[start:], summVersion)
            start += advanced
            begin += advanced
            numbers.append(number)


    elif length_type_ID == "1":
        length = binary_string[start: start + 11]
        start += 11
        number_packets = int(length,2)
        print("Visiting",number_packets,"packets")
        numbers = []
        for i in range(number_packets):
            print("Enter Subpacket by number : ", binary_string[start:])
            number, advanced, summVersion = uncode_binary(binary_string[start:], summVersion)
            start += advanced
            numbers.append(number)

    # Operations on subpackets
    if type_ID == 0:
        value = sum(numbers)

    elif type_ID == 1:
        value = 1
        for x in numbers:
            value = value * x

    elif type_ID == 2:
        value = min(numbers)

    elif type_ID == 3:
        value = max(numbers)

    elif type_ID == 5:
        if numbers[0] > numbers[1]:
            value = 1
        else:
            value = 0

    elif type_ID == 6:
        if numbers[0] < numbers[1]:
            value = 1
        else:
            value = 0
    
    elif type_ID == 7:
        if numbers[0] == numbers[1]:
            value = 1
        else:
            value = 0


    return value, start, summVersion

def uncode_binary(binary_string, summVersion):
    version = int(binary_string[0:3],2)
    type_ID = int(binary_string[3:6],2)
    summVersion += version
    print("Version :", version)
    print("Type :", type_ID)
    if type_ID == 4:
        value, start = read_litteral(binary_string, 6)
        print("Value :", value)
        return value, start, summVersion
    else:
        value, start, summVersion = read_operator(type_ID, binary_string, 6, summVersion)
        print("Values :", value)
        return value, start, summVersion



    

def part1(binary_string):
    print(binary_string)
    summVersion = 0
    values, start, summVersion = uncode_binary(binary_string, summVersion)

    return summVersion
 

def part2(binary_string):
    
    print(binary_string)
    summVersion = 0
    values, start, summVersion = uncode_binary(binary_string, summVersion)

    return values
 

## Select function here :
if __name__ == "__main__":
    binary_string = transform_data(f)
    print("Sum of Version : ", part1(binary_string))
    print("Final value : ", part2(binary_string))


