from Student import Student

if __name__ == '__main__':
    for data in open('.\\students.txt'):
        spli_data = data.split(',')
        if len(spli_data) == 5:
            Student(spli_data[0], spli_data[1], spli_data[2], float(spli_data[3]), float(spli_data[4]))
        elif len(spli_data) == 6:
            Student(spli_data[0], spli_data[1], spli_data[2], float(spli_data[3]), float(spli_data[4]), spli_data[5])
        else:
            Student(spli_data[0], spli_data[1], spli_data[2], float(spli_data[3]))

    Student.grade()
    print(Student.add_new_student('test@gmail.com', '1', '1', 70, 3.5, 'MAILED'))
    print(f"created: {Student.add_new_student('lalala', 'kamil', 'kaminski', 70, 3.5, 'MAILED')}")
    Student.delete_student('lalala')

    for s in Student.students:
        print(s)