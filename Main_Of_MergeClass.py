from Merge_Between_OOP_And_Files_Write import  Student
def main ():
    s1 = Student()
    s2 = Student()
    file = open("Student.txt" , 'a')
    s1.enter("kamel" , 111)
    s2.enter("ahmed" , 222)
    file.write(s1.get_info() + "\n")
    file.write(s2.get_info() + "\n")
    file.close()
    print("Writing Suceesfully")



if __name__ == '__main__':
    main()