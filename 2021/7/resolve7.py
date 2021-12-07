import numpy as n
f = open("input.txt", "r")

def transform_data(arg):
    list_crabs = list(map(int, arg.readline().split(',')))

    return list_crabs

def part1(list_crabs):

    minimal_value = min(list_crabs)
    maximal_value = max(list_crabs)
    
    #Brut Force version
    
    best_fuel = maximal_value
    for i in range(maximal_value - minimal_value):
        target = minimal_value + i
        fuel = 0
        for crab in list_crabs:
            fuel += (crab - target) if (crab > target) else (target - crab)
            

        #first iteration
        if target == minimal_value:
            best_fuel = fuel

        if fuel < best_fuel:
            best_fuel = fuel 
        
    return best_fuel


def part2(list_crabs):

    minimal_value = min(list_crabs)
    maximal_value = max(list_crabs)
    
    #Brut Force version
    
    best_fuel = maximal_value
    for i in range(maximal_value - minimal_value):
        target = minimal_value + i
        fuel = 0
        for crab in list_crabs:
            difference = (crab - target) if (crab > target) else (target - crab)

            fuel += int((difference*(difference+1))/2)
            

        #first iteration
        if target == minimal_value:
            best_fuel = fuel

        if fuel < best_fuel:
            best_fuel = fuel 
         
    return best_fuel
 

## Select function here :
if __name__ == "__main__":  
    list_crabs = transform_data(f)
    print("result1 = ", part1(list_crabs))
    print("result2 = ", part2(list_crabs))

