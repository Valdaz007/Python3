def main():
    list0 = [20, 5, 10, 16, 3, 22, 47, 13, 6, 9]
    list0 = mergesort(list0)
    print(list0)

def merge(left, right, array):
    lenOfLeft = len(left)
    lenOfRight = len(right)

    posArray = 0; posMinLeft = 0; posMinRight = 0

    while posMinLeft < lenOfLeft and posMinRight < lenOfRight:
        if left[posMinLeft] <= right[posMinRight]:
            array[posArray] = left[posMinLeft]
            posMinLeft += 1
        else:
            array[posArray] = right[posMinRight]
            posMinRight += 1
        posArray += 1
    
    while posMinLeft < lenOfLeft:
        array[posArray] = left[posMinLeft]
        posMinLeft += 1
        posArray += 1

    while posMinRight < lenOfRight:
        array[posArray] = right[posMinRight]
        posMinRight += 1
        posArray += 1

def mergesort(array):
    lenght = len(array)
    if lenght < 2:
        return 0
    
    mid = lenght//2
    leftarray = array[0:mid]
    rightarray = array[mid:lenght]

    mergesort(leftarray)
    mergesort(rightarray)
    merge(leftarray, rightarray, array)
    if len(array) == lenght:
        return array

if __name__ == "__main__":
    main()