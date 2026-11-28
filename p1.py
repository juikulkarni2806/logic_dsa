def get_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=40:
        return "D"
    else:
        return "F"
class Node:
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
        self.grade=get_grade(marks)
        self.next=None

class StudentList:
    def __init__(self):
        self.head=None

    def print_students(self,s):
        print(f"Roll Number:{s.roll},Name:{s.name},Marks:{s.marks},Grade:{s.grade}")
    
    def search(self,roll):
        temp=self.head
        while temp:
            if temp.roll==roll:
                return temp
            temp=temp.next
        return None
    
    def add_students(self,roll,name,marks):
        if self.search(roll):
            print("Student Already Exists!")
            return
        new=Node(roll,name,marks)
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
        print(f"New Student Added.\nGrade:{new.grade}")

    def search_student(self,roll):
        s=self.search(roll)
        if s:
            print(f"Student Found:{s.roll}")
            return
        else:
            print("Student Not Found!")

    def update_marks(self,roll,marks):
        s=self.search(roll)
        if s:
            s.marks=marks
            s.grade=get_grade(marks)
            print(f"Student's Marks Updated\n New Grade:{s.grade}")
        else:
            print("Student not Found!")
    
    def delete_student(self,roll):
        temp=self.head
        prev=None
        while temp and temp.roll!=roll:
            prev=temp
            temp=temp.next
        if temp is None:
            print("Student not Found!")
            return
        if prev is None:
            self.head=temp.next
        else:
            prev.next=temp.next
        print("Student Deleted.")

    def display_all(self):
        if self.head is None:
            print("No Students.")
        temp=self.head
        while temp:
            self.print_students(temp)
            temp=temp.next
    
    def topper(self):
        if self.head is None:
            print("No Students")
            return
        best=self.head
        temp=self.head.next
        while temp:
            if temp.marks>best.marks:
                best=temp
            temp=temp.next
        print(f"Topper:{best.name}\n Marks:{best.marks} with Grade:{best.grade}")

    def below_passing(self, passing_mark):
        temp = self.head
        found = False
        while temp:
            if temp.marks < passing_mark:
                self.print_student(temp)
                found = True
            temp = temp.next
        if not found:
            print("No students below passing mark.")


students = StudentList()

while True:
    print("\n1.Add  2.Search  3.Update Marks  4.Delete  5.Display All  6.Topper  7.Below Passing  0.Exit")
    ch = input("Choice: ")

    if ch == "1":
        roll = int(input("Roll: "))
        name = input("Name: ")
        marks = int(input("Marks: "))
        students.add_students(roll, name, marks)
    elif ch == "2":
        students.search_student(int(input("Roll: ")))
    elif ch == "3":
        roll = int(input("Roll: "))
        marks = int(input("New Marks: "))
        students.update_marks(roll, marks)
    elif ch == "4":
        students.delete_student(int(input("Roll: ")))
    elif ch == "5":
        students.display_all()
    elif ch == "6":
        students.topper()
    elif ch == "7":
        students.below_passing(int(input("Passing mark: ")))
    elif ch == "0":
        break
    else:
        print("Invalid choice.")

        




        


    