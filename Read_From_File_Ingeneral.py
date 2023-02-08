def main ():
    file = open("student.txt",'r') # r mean read
    print(file.read(3))       # read all data in the file
    print(file.readline())   # For read one line only
    print(file.readline())
    print(file.name)
    print(file.mode)
    print(file.encoding)
    file.close()



if __name__ == '__main__':
    main()