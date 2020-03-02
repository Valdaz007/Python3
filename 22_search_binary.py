import VCode

def main():
    list0 = [20, 5, 10, 16, 3, 22, 47, 13, 6, 9]
    list0 = VCode.mergesort(list0)
    print(list0)
    print(binary(22, list0))

def binary(value, values):
    startOfArray = 0; endOfArray = len(values) - 1

    while startOfArray <= endOfArray:
        mid_index = (startOfArray + endOfArray)//2
        if values[mid_index] == value:
            return ("Value {} Found in Index {}.".format(value, mid_index))
        elif values[mid_index] > value:
            endOfArray = mid_index - 1
        else: 
            startOfArray = mid_index + 1
    return ("Value {} Not Found in List.".format(value))

if __name__ == "__main__":
    main()