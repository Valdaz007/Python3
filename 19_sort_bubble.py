def main():
    list0 = [20, 5, 10, 16, 3, 22, 47, 13, 6, 9]

    print(bubble(list0))

def bubble(values):
    for i in range(len(values)):
        for j in range(len(values)-1):
            if values[j] > values[j+1]:
                temp = values[j]
                values[j] = values[j+1]
                values[j+1] = temp
    return values

if __name__ == "__main__":
    main()