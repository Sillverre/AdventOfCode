f = open("input.txt", "r")

def transform_data(arg):
    lines = []

    for line in arg:
        lines.append(line)

    return lines

def is_open(char):
    if char == '{' or char == '(' or char == '<' or char == '[':
        return True
    return False

def is_close(char):
    if char == '}' or char == ')' or char == '>' or char == ']':
        return True
    return False

def scoring(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137
    else:
        return 0

def scoring_completion(char):
    if char == ')':
        return 1
    elif char == ']':
        return 2
    elif char == '}':
        return 3
    elif char == '>':
        return 4
    else:
        return 0

def entry_To_Close(entry):
    closing =[]
    for char in entry[::-1]:
        new_char = open_Find_Close(char)
        closing.append(new_char)

    return closing


def close_Find_Open(exit_char):
    if exit_char == ')':
        return '('
    elif exit_char == ']':
        return '['
    elif exit_char == '}':
        return '{'
    elif exit_char == '>':
        return '<'
    else:
        return ''

def open_Find_Close(open_char):
    if open_char == '(':
        return ')'
    elif open_char == '[':
        return ']'
    elif open_char == '{':
        return '}'
    elif open_char == '<':
        return '>'
    else:
        return ''


def part1_2(arg):
    lines = transform_data(arg)
    score = 0
    completion_scores = []
    for line in lines:
        entry = []
        line_as_list = list(line.strip())
        is_corrupted = False
        for char in line_as_list:
            # Add new 
            if is_open(char):
                entry.append(char)
            else:
                # Illegal detected
                if close_Find_Open(char) != entry[-1]:
                    score += scoring(char)
                    is_corrupted = True
                    break
                # Normally Closed
                else :
                    entry.pop()
            
        
        if not is_corrupted:
            remaining = entry_To_Close(entry)
            score2 = 0

            for char in remaining:
                score2 = score2 * 5
                score2 += scoring_completion(char)
            completion_scores.append(score2)
    
    completion_scores.sort()
    middle_score = completion_scores[len(completion_scores)//2]
    return score , middle_score

 
## Select function here :
print(part1_2(f))

