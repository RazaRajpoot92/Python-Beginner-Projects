def main(list, element):
    
    start = 0
    end = len(list)
    middle = 0
    steps = 0
    
    while(start <= end):
        print(f"{steps}: {list[start: end]}")
        steps += 1
        middle = (start + end) // 2
        if element == list[middle]:
            print(list[middle])
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle +1
    return -1


l = [1,2,3,4,5,6,7,8,9]

main(l, 6)            