def main():
    filename = input('Enter the name of the file: ')
    line_max = 5
    test_file = open(filename, 'r')

    for i in range(line_max): 
        print(test_file.readline())
        print(test_file.readline())
        print(test_file.readline())
        print(test_file.readline())
        print(test_file.readline())
        

main()