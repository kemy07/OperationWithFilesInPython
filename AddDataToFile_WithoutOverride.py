def main ():
    file = open("Student.txt",'a') #a mean append
    name = input("Please Enter a Student name \n")
    id = int (input("Please Enter student number \n"))
    file.write("Name : " + name + "\n")
    file.write("Id : " + str (id) + "\n")
    file.write("______________________" + "\n")
    file.close()

if __name__ == '__main__':
    main()