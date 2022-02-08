import numbers


def BinarySearch(numbers,target):
    left,right = 0,len(numbers)-1
    while left<=right:
        mid= int(left+(right-left)/2)

        if target == numbers[mid]:
            return mid
        elif target <numbers[mid]:
            right=mid-1
        else:
            left = mid+1
    return -1

if __name__ == '__main__':
    numbers = [1,4,5,7,8,9,12,34,56,76,87,545,6543,7653,86765,132132]
    target = 545

    position = BinarySearch(numbers,target)

    if position != -1:
        print("The position of Target element is:",position)    
    else:
        print("The Target element is not present.")