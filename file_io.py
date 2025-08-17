import os

def save_students(students: dict, filename: str = "students.txt") -> None:
    """把字典保存为文本文件"""
    with open(filename, "w", encoding="utf-8") as f:
        for sid, info in students.items():
            line = f"{sid},{info[0]},{info[1]},{info[2]}\n"
            f.write(line)
    print("数据已保存！")

def load_students(filename: str = "students.txt") -> dict:
    """从文本文件加载字典"""
    students = {}
    if not os.path.exists(filename):
        return students
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            sid, name, gender, age = line.strip().split(",")
            students[sid] = [name, gender, age]
    print("数据已加载！")
    return students