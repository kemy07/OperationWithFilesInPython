from Read_Data_From_File_using_OOP import myStudent
def main ():
    stud = []
    # s1 = myStudent()
    # s2 = myStudent()
    # s3 = myStudent()
    file = open("mystudent.txt" , 'r')
    for i in range (2):
        s = myStudent()
        s.enter(file.readline() , int (file.readline()))
        stud.append(s)
    # s2.enter(file.readline() , int (file.readline()))
    # s3.enter(file.readline() , int (file.readline()))
    print("Students Details" +"\n")
    for i in range (2):
        stud[i].display()
    # print("Students Details \n")
    # s1.display()
    # s2.display()
    # s3.display()
    file.close()



if __name__ == '__main__':
    main()