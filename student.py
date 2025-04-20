class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.department = ""
        self.mobile_no = ""

    def read_student_info(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.department = input("Enter department: ")
        self.mobile_no = input("Enter mobile number: ")

    def print_student_info(self):
        print("\nStudent Information:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Department:", self.department)
        print("Mobile Number:", self.mobile_no)


# Create an instance of the Student class
student = Student()

# Read and set student information
student.read_student_info()

# Print student information
student.print_student_info()
