def main():
    list0 = [20, 5, 10, 16, 3, 22, 47, 13, 6, 9]

    print(selection(list0))

def selection(values):
    for i in range(len(values)):
        min_index = i
        for j in range(i+1,len(values)):
            if values[min_index] > values[j]:
                min_index = j
        temp = values[i]
        values[i] = values[min_index]
        values[min_index] = temp
    return values

if __name__ == "__main__":
    main()