import copy as cp

f = open("input.txt", "r")

## PART 2 NOT WORKING

def transform_data(arg):
    enhancement = list(arg.readline().strip())
    # empty line
    arg.readline()
    image = []
    for line in arg.readlines():
        image.append(list(line.strip()))
    
    return enhancement, image

def encapsule(image,scope):
    bigger_image = []

    for i in range(scope):
        firstLine = ['.' for j in range(len(image[0]) + (2 * scope))]
        bigger_image.append(firstLine)

    for i in range(len(image)):
        line = cp.deepcopy(image[i])

        for k in range(scope):
            line.insert(0,'.')
            line.insert(len(line),'.')

        bigger_image.append(line)

    for i in range(scope):
        lastLine = ['.' for j in range(len(image[0]) + (2 * scope))]
        bigger_image.append(lastLine)

    return bigger_image
        

def get_index_enhance(i, j, image):

    first_line = "".join(image[i-1][j-1:j+2])
    middle_line = "".join(image[i][j-1:j+2])
    last_line = "".join(image[i+1][j-1:j+2])

    """
    print(first_line)
    print(middle_line)
    print(last_line)
    print(i,j)
    """

    combined = first_line + middle_line + last_line
    combined = combined.replace('.','0').replace('#','1')
    
    index_enhance = int("0b" + combined, 2)
    return index_enhance

def read_input(enhancement, image):

    image_copy = cp.deepcopy(image)

    for i in range(1,len(image)-1):
        for j in range(1,len(image[0])-1):
            index = get_index_enhance(i, j, image)
            
            image_copy[i][j] = enhancement[index]
    return image_copy

def print_image(image):
    for i in image:
        print(''.join(map(str, i)))

def count_pixels(image, edge_margin):
    summ = 0

    for i in range(edge_margin, len(image) - edge_margin)  :
            summ += image[i][edge_margin:-edge_margin].count("#")
    return summ

def part1(arg):
    enhancement, image = transform_data(arg)
    print_image(image)
    iteration = 2
    edge_margin = 6
    image = encapsule(image, edge_margin)
    for i in range(iteration):
        image = read_input(enhancement, encapsule(image,1))
        print_image(image)
 
    return(count_pixels(image, edge_margin))

def part2(arg):
    enhancement, image = transform_data(arg)
    print_image(image)
    iteration = 50
    edge_margin = 3 # Idea : change bit 0
    image = encapsule(image, edge_margin)
    for i in range(iteration):
        image = read_input(enhancement, encapsule(image,1))
        # print_image(image)
 
    return(count_pixels(image, edge_margin))

 

## Select function here :
if __name__ == "__main__":
    print(part2(f))


