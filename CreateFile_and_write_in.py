def main ():
    name = input("Please Enter File name Like name \n")
    file = open(name+ ".txt",'w') #w mean write
    file.write("This Is a file Written by Python")
    file.close()

if __name__ == '__main__':
    main()