def main():
    list0 = [20, 5, 10, 16, 3, 22, 47, 13, 6, 9]

    print(linear(2, list0))
    

def linear(value, values):
    for i in range(len(values)):
        if values[i] == value:
            return ("Value {} found in index {}.".format(value, i))
    return ("Value {} not found in the list.".format(value))

if __name__ == "__main__":
    main()