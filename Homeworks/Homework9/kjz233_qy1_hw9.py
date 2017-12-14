

class Student:
    def __init__(self,name,NYU_id,net_id):
        self.name = name
        self.NYU_id = NYU_id
        self.net_id = net_id
        self.grades_list = []
    def add_grade(self,catalog_name,grade):
        grade = (catalog_name,int(grade))
        self.grades_list.append(grade)
        return grade
    def average(self):
        sumGrade = 0
        classes = 0
        average = 0
        for student in load:
            if self.name == student.name:
                for courseGrade in student.grades_list:
                    sumGrade += courseGrade[1]
                    classes += 1
        average = round(sumGrade / classes,0)
        return average
    def get_email(self):
        email = str(self.net_id)+"@nyu.edu"
        return email

def load_students(students_data_filename):
    studentList = []
    studentsInfo = open(students_data_filename,"r")
    firstLine = studentsInfo.readline()
    firstLine = firstLine[0:-1]
    header = firstLine.split(",")
    for line in studentsInfo:
        line = line[0:-1]
        item = line.split(",")
        student = Student(name=item[1], NYU_id=item[0], net_id=item[2])
        index = 3
        grades = item[3:10]
        for grade in item[3:10]:
            #print(grade)
            if grade != "":
                student.add_grade(catalog_name=header[index],grade=grade)
                index += 1
                #print(grade)
            else:
                index += 1
        studentList.append(student)
    #print(studentList)
    #print(gradeList)
    studentsInfo.close()
    return studentList

load = load_students("hw9 - students_grades.csv")
#print(load)
def generate_performance_report(students_lst, out_filename):
    cleanReport = open(out_filename, "w")
    print("NYU ID,Average", file=cleanReport)
    for student in students_lst:
        #print(student)
        studentClass = Student(name=student.name,NYU_id=student.NYU_id,net_id=student.net_id)
        #print(student[1])
        grades = student.grades_list
        #print(grades)
        avgScore = str(studentClass.average())
        print(student.NYU_id + "," + avgScore, file=cleanReport)


generate_performance_report(load,"performance_report.csv")

def generate_course_mailing_list(students_lst, catalog_name,out_filename):
    cleanMailing = open(out_filename, "w")
    for student in students_lst:
        studentClass = Student(student.name,student.NYU_id,student.net_id)
        #print(student)
        courseGrades = student.grades_list
        for course in courseGrades:
            if course[0] == catalog_name:
                #print(course[0])
                print(studentClass.get_email(),file=cleanMailing)

generate_course_mailing_list(load,"CS-UY 1114","course_mailing_list.txt")

def main():
    load = load_students("hw9 - students_grades.csv")
    students_lst = load
    generate_performance_report(students_lst, "performance_report.csv")
    course = input("Which course would you like the mailing list to be for? ")
    catalog_name = course
    generate_course_mailing_list(students_lst,catalog_name, "course_mailing_list.txt")
