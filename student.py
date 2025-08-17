# 在这里写上你的代码 :-)
def add_student(students:dict):
    """添加学生到学籍字典"""
    sid = input("请输入编号：")
    name = input("请输入名字：")
    gender = input("请输入性别：")
    age = input("请输入年龄：")
    students[sid] = [name,gender,age]
    print("添加成功当前学生：", students[sid])
def query_student(students:dict)->None:
    """根据编号查询学生信息"""
    sid = input("请输入编号：")
    info = students.get(sid)
    if info:
        print(f"您输入的学生编号{sid}信息：姓名={info[0]},性别={info[1]},年龄={info[2]}")
    else:
        print("未找到该学生！")
def update_student(students: dict) -> None:
    """修改学生信息"""
    sid = input("请输入编号：")
    if sid in students:
        name = input("请输入名字：")
        gender = input("请输入性别：")
        age = input("请输入年龄：")
        students[sid] = [name,gender,age]
        print("修改成功!")
    else:
        print("未找到该学生！")
def delete_student(students: dict) -> None:
    """删除学生记录"""
    bmhc = input("请输入要删除的编号：")
    if bmhc in students:
        students.pop(bmhc)
    else:
        print("未找到该学生！")