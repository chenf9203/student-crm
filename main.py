# 在这里写上你的代码 :-)
if __name__ == "__main__":
    from student import edd_student,query_student,update_student,delete_student
    students = {}
    while True:
        choice = input("1.添加，2.查询，3.修改，4.删除，5，结束，请输入：")
        if choice == "1":
            edd_student(students)
        elif choice == "2":
            query_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("再见")
            break
        else:
            print("请输入1-5之间")
