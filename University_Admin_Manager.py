import tkinter
import customtkinter
import mysql.connector

#Connect to the locally hosted database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jordan&Javier!!",
        port="3306",
        auth_plugin="mysql_native_password",
        database="431wproject"
    )

#App Appeareance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Elements in the frame (Buttons, etc)
class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #1. Add a student into the database, lines 26-79
        #Add Student Heading/Title
        addStudent_title = customtkinter.CTkLabel(self, text="Insert Student Information", font=("Arial", 20, "bold"))
        addStudent_title.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        #Label for entering student id
        student_id_label = customtkinter.CTkLabel(self, text="Enter Student ID:", font=("Arial", 12))
        student_id_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the student id
        student_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 111110 (6 digits)", font=("Arial", 12))
        student_id_entry.grid(row=2, column=1, padx=10, pady=5)

        #Label for entering student first name
        first_name_label = customtkinter.CTkLabel(self, text="Enter First Name:", font=("Arial", 12))
        first_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the student first name
        first_name_entry = customtkinter.CTkEntry(self, placeholder_text="e.g John", font=("Arial", 12))
        first_name_entry.grid(row=3, column=1, padx=10, pady=5)

        #Label for entering student last name
        last_name_label = customtkinter.CTkLabel(self, text="Enter Last Name:", font=("Arial", 12))
        last_name_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the student last name
        last_name_entry = customtkinter.CTkEntry(self, placeholder_text="e.g Doe", font=("Arial", 12))
        last_name_entry.grid(row=4, column=1, padx=10, pady=5)

        #Label for entering the student major
        major_label = customtkinter.CTkLabel(self, text="Enter Major:", font=("Arial", 12))
        major_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the student major
        major_entry = customtkinter.CTkEntry(self, placeholder_text="e.g CMPSC", font=("Arial", 12))
        major_entry.grid(row=5, column=1, padx=10, pady=5)

        #Label for entering the student's year
        year_label = customtkinter.CTkLabel(self, text="Enter Year:", font=("Arial", 12))
        year_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering the student's year
        year_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 1 (1, 2, 3, or 4)", font=("Arial", 12))
        year_entry.grid(row=6, column=1, padx=10, pady=5)

        #Label for entering the student's GPA
        GPA_label = customtkinter.CTkLabel(self, text="Enter GPA:", font=("Arial", 12))
        GPA_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering student's GPA
        GPA_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 3.5", font=("Arial", 12))
        GPA_entry.grid(row=7, column=1, padx=10, pady=5)

        #Label to display if the entry was succesful or a failure (with error)
        add_student_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        add_student_result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        #A button to add the student information from the entered fields
        add_student_button = customtkinter.CTkButton(self, text="Add Student", command=lambda: addStudent(student_id_entry, first_name_entry, last_name_entry, major_entry, year_entry, GPA_entry, add_student_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        add_student_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        ##############################################################################

        #2. Remove a course from the database, lines 83-101
        #Remove Course heading/title
        remove_Course_title = customtkinter.CTkLabel(self, text="Remove Course", font=("Arial", 20, "bold"))
        remove_Course_title.grid(row=10, column=0, columnspan=2, padx=10, pady=20)

        #Label for entering the course id
        course_id_label = customtkinter.CTkLabel(self, text="Enter Course ID to be Removed:", font=("Arial", 12))
        course_id_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering the course id
        course_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 123450 (6 Digits)", font=("Arial", 12))
        course_id_entry.grid(row=11, column=1, padx=10, pady=5)

        #Label to display if the removal was successful or a failure (with error)
        remove_Course_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        remove_Course_result_label.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        #A button to remove the course from the course information
        remove_Course_button = customtkinter.CTkButton(self, text="Remove Course", command=lambda: removeCourse(course_id_entry, remove_Course_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        remove_Course_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

        ####################################################################################

        #3. Update a students information in the database, lines 105-158
        #Update student information heading/title
        updateStudent_title = customtkinter.CTkLabel(self, text="Update Student Information", font=("Arial", 20, "bold"))
        updateStudent_title.grid(row=14, column=0, columnspan=2, padx=10, pady=20)
        
        #Label for entering the student id
        update_student_id_label = customtkinter.CTkLabel(self, text="Enter Student ID to Update:", font=("Arial", 12))
        update_student_id_label.grid(row=15, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the student id
        update_student_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 111110 (6 digits)", font=("Arial", 12))
        update_student_id_entry.grid(row=15, column=1, padx=10, pady=5)
        
        #Label for entering the students first name
        update_first_name_label = customtkinter.CTkLabel(self, text="Enter New First Name:", font=("Arial", 12))
        update_first_name_label.grid(row=16, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the students first name
        update_first_name_entry = customtkinter.CTkEntry(self, placeholder_text="e.g John", font=("Arial", 12))
        update_first_name_entry.grid(row=16, column=1, padx=10, pady=5)
        
        #Label for entering the students last name
        update_last_name_label = customtkinter.CTkLabel(self, text="Enter New Last Name:", font=("Arial", 12))
        update_last_name_label.grid(row=17, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the students last name
        update_last_name_entry = customtkinter.CTkEntry(self, placeholder_text="e.g Doe", font=("Arial", 12))
        update_last_name_entry.grid(row=17, column=1, padx=10, pady=5)

        #Label for entering the students major
        update_major_label = customtkinter.CTkLabel(self, text="Enter New Major:", font=("Arial", 12))
        update_major_label.grid(row=18, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering the students major
        update_major_entry = customtkinter.CTkEntry(self, placeholder_text="e.g CMPSC", font=("Arial", 12))
        update_major_entry.grid(row=18, column=1, padx=10, pady=5)
        
        #Label for entering the students year
        update_year_label = customtkinter.CTkLabel(self, text="Enter New Year:", font=("Arial", 12))
        update_year_label.grid(row=19, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the students year
        update_year_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 1 (1, 2, 3, or 4)", font=("Arial", 12))
        update_year_entry.grid(row=19, column=1, padx=10, pady=5)

        #Label for entering the student's GPA
        update_GPA_label = customtkinter.CTkLabel(self, text="Enter New GPA:", font=("Arial", 12))
        update_GPA_label.grid(row=20, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering student's GPA
        update_GPA_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 3.5", font=("Arial", 12))
        update_GPA_entry.grid(row=20, column=1, padx=10, pady=5)
        
        #Lable to display if updating the students information was successful or a failure (with error)
        update_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        update_result_label.grid(row=21, column=0, columnspan=2, padx=10, pady=10)
        
        #A button to update the students information in the database
        update_button = customtkinter.CTkButton(self, text="Update Student Information", command=lambda: updateStudent(update_student_id_entry, update_first_name_entry, update_last_name_entry, update_major_entry, update_year_entry, update_GPA_entry, update_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        update_button.grid(row=22, column=0, columnspan=2, padx=10, pady=10)

        ####################################################################################

        #4. Generate a GPA report from highest to lowest, lines 162-173
        #Generate the GPA report heading/title
        generate_GPA_report_title = customtkinter.CTkLabel(self, text="Generate GPA Report", font=("Arial", 20, "bold"))
        generate_GPA_report_title.grid(row=23, column=0, columnspan=2, padx=10, pady=20)

        #Label to display the output of the GPA report or if an error occurred
        GPA_report_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        GPA_report_result_label.grid(row=24, column=0, columnspan=2, padx=10, pady=10)

        #Button to display the GPA report to the user
        generate_GPA_report_button = customtkinter.CTkButton(self, text="Generate GPA Report", command=lambda: generateGPAReport(GPA_report_result_label),font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        generate_GPA_report_button.grid(row=25, column=0, columnspan=2, padx=10, pady=10)

        ######################################################################################

        #5. Delete a student from the database, lines 176-194
        #Remove Student heading/title
        remove_Student_title = customtkinter.CTkLabel(self, text="Remove Student", font=("Arial", 20, "bold"))
        remove_Student_title.grid(row=26, column=0, columnspan=2, padx=10, pady=20)

        #Label for entering the student id
        remove_Student_id_label = customtkinter.CTkLabel(self, text="Enter Student ID to be Removed:", font=("Arial", 12))
        remove_Student_id_label.grid(row=27, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering the student id
        remove_student_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 111110 (6 Digits)", font=("Arial", 12))
        remove_student_id_entry.grid(row=27, column=1, padx=10, pady=5)

        #Label to display if the removal was successful or a failure (with error)
        remove_student_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        remove_student_result_label.grid(row=28, column=0, columnspan=2, padx=10, pady=10)

        #A button to remove the course from the course information
        remove_student_button = customtkinter.CTkButton(self, text="Remove Student", command=lambda: removeStudent(remove_student_id_entry, remove_student_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        remove_student_button.grid(row=29, column=0, columnspan=2, padx=10, pady=10)

        ##################################################################################################

        #6. Add a course to the database, lines 198-251
        #Add Student Heading/Title
        addCourse_title = customtkinter.CTkLabel(self, text="Insert Course Information", font=("Arial", 20, "bold"))
        addCourse_title.grid(row=30, column=0, columnspan=2, padx=10, pady=20)

        #Label for entering course id
        course_id_label = customtkinter.CTkLabel(self, text="Enter Course ID:", font=("Arial", 12))
        course_id_label.grid(row=31, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the course id
        course_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 123450 (6 digits)", font=("Arial", 12))
        course_id_entry.grid(row=31, column=1, padx=10, pady=5)

        #Label for entering course  name
        course_name_label = customtkinter.CTkLabel(self, text="Enter Course Name:", font=("Arial", 12))
        course_name_label.grid(row=32, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the course name
        course_name_entry = customtkinter.CTkEntry(self, placeholder_text="e.g CMPSC", font=("Arial", 12))
        course_name_entry.grid(row=32, column=1, padx=10, pady=5)

        #Label for entering course code
        course_code_label = customtkinter.CTkLabel(self, text="Enter course code:", font=("Arial", 12))
        course_code_label.grid(row=33, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the course code
        course_code_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 464", font=("Arial", 12))
        course_code_entry.grid(row=33, column=1, padx=10, pady=5)

        #Label for entering the department id
        department_id_label = customtkinter.CTkLabel(self, text="Enter Department ID:", font=("Arial", 12))
        department_id_label.grid(row=34, column=0, padx=10, pady=5, sticky="w")
        #Entry field to enter the department id
        department_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 1210 (4 Digits)", font=("Arial", 12))
        department_id_entry.grid(row=34, column=1, padx=10, pady=5)

        #Label for entering the credit hours
        credit_hours_label = customtkinter.CTkLabel(self, text="Enter Credit Hours:", font=("Arial", 12))
        credit_hours_label.grid(row=35, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering the credit hours
        credit_hours_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 1 (1, 2, 3, or 4)", font=("Arial", 12))
        credit_hours_entry.grid(row=35, column=1, padx=10, pady=5)

        #Label for entering the instructor id
        instructor_id_label = customtkinter.CTkLabel(self, text="Enter Instructor ID:", font=("Arial", 12))
        instructor_id_label.grid(row=36, column=0, padx=10, pady=5, sticky="w")
        #Entry field for entering the instructor id
        instructor_id_entry = customtkinter.CTkEntry(self, placeholder_text="e.g 21310 (5 Digits)", font=("Arial", 12))
        instructor_id_entry.grid(row=36, column=1, padx=10, pady=5)

        #Label to display if the entry was succesful or a failure (with error)
        add_course_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        add_course_result_label.grid(row=37, column=0, columnspan=2, padx=10, pady=10)

        #A button to add the student information from the entered fields
        add_course_button = customtkinter.CTkButton(self, text="Add Course", command=lambda: addCourse(course_id_entry, course_name_entry, course_code_entry, department_id_entry, credit_hours_entry, instructor_id_entry, add_course_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        add_course_button.grid(row=38, column=0, columnspan=2, padx=10, pady=10)

        #########################################################################################################

        #7. Generate a courses report, lines 255-266
        #Generate the courses report heading/title
        generate_course_report_title = customtkinter.CTkLabel(self, text="Generate Courses Report", font=("Arial", 20, "bold"))
        generate_course_report_title.grid(row=39, column=0, columnspan=2, padx=10, pady=20)

        #Label to display the output of the course report or if an error occurred
        course_report_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        course_report_result_label.grid(row=40, column=0, columnspan=2, padx=10, pady=10)

        #Button to display the course report to the user
        generate_course_report_button = customtkinter.CTkButton(self, text="Generate Course Report", command=lambda: generateCourseReport(course_report_result_label),font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        generate_course_report_button.grid(row=41, column=0, columnspan=2, padx=10, pady=10)

        ####################################################################################################

        #8. Generate a enrolled courses report, lines 270-288
        #Generate the enrolled courses report heading/title
        generate_enroll_course_report_title = customtkinter.CTkLabel(self, text="Generate Enrolled Courses Report", font=("Arial", 20, "bold"))
        generate_enroll_course_report_title.grid(row=42, column=0, columnspan=2, padx=10, pady=20)

        #Label for entering the course id
        enroll_course_id_label = customtkinter.CTkLabel(self, text="Enter Course ID:", font=("Arial", 12))
        enroll_course_id_label.grid(row=43, column=0, padx=10, pady=5)
        #Entry field to enter the course id
        enroll_course_id_entry = customtkinter.CTkEntry(self,  placeholder_text="e.g 123450 (6 Digits)", font=("Arial", 12))
        enroll_course_id_entry.grid(row=43, column=1, padx=10, pady=5)

        #Label to display the output of the enrolled courses report or if an error occured
        enroll_course_report_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        enroll_course_report_result_label.grid(row=44, column=0, columnspan=2, padx=10, pady=10)

        #A button to do the action of generating the enrolled courses report
        generate_enroll_course_report_button = customtkinter.CTkButton(self, text="Generate Enrolled Course Report", command=lambda: generateEnrolledCourseReport(enroll_course_id_entry, enroll_course_report_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        generate_enroll_course_report_button.grid(row=45, column=0, columnspan=2, padx=10, pady=10)
        
     #################################################################################################################

        #9. Generate a specific student information report 
        #Generate the student information report heading/title
        generate_student_information_report_title = customtkinter.CTkLabel(self, text="Generate Student Information Report", font=("Arial", 20, "bold"))
        generate_student_information_report_title.grid(row=46, column=0, columnspan=2, padx=10, pady=20)

        #Label for entering the student id
        information_student_id_label = customtkinter.CTkLabel(self, text="Enter Student ID:", font=("Arial", 12))
        information_student_id_label.grid(row=47, column=0, padx=10, pady=5)
        #Entry field to enter the student id
        information_student_id_entry = customtkinter.CTkEntry(self,  placeholder_text="e.g 111110 (6 Digits)", font=("Arial", 12))
        information_student_id_entry.grid(row=47, column=1, padx=10, pady=5)

        #Label to display the output of the student informatiom report or if an error occured
        student_information_report_result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        student_information_report_result_label.grid(row=48, column=0, columnspan=2, padx=10, pady=10)

        #A button to do the action of generating the student information report
        generate_student_information_report_button = customtkinter.CTkButton(self, text="Generate Student Information Report", command=lambda: generateStudentInformationReport(information_student_id_entry, student_information_report_result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        generate_student_information_report_button.grid(row=49, column=0, columnspan=2, padx=10, pady=10)

#Sets Up the App appearance
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Window Title
        self.title("University Administration Manager")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Size of the window
        self.my_frame = MyFrame(master=self, width=700, height=480, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")

#1. Function to add a student into the database
def addStudent(student_id_entry, first_name_entry, last_name_entry, major_entry, year_entry, GPA_entry, result_label):
    #Retrieve the user inputted information 
    student_id = student_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    major = major_entry.get()
    year = year_entry.get()
    gpa = GPA_entry.get()

    #Error to handle if one of the entry fields are empty or NULL. All Entry fields must be filled.
    if not student_id or not first_name or not last_name or not major or not year or not gpa:
        result_label.config(text="All Entry fields are required.")
        return

    #Connect to the database and try to add the student
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to insert the student into the database
        cursor.execute(""" 
            INSERT INTO studentinformation (StudentID, StuFirstName, StuLastName, Major, Year, GPA) 
            VALUES (%s, %s, %s, %s, %s, %s)""", (student_id, first_name, last_name, major, year, gpa))

        #Finializes the changes to the database
        db.commit()

        #Returns that it was complete, with the students name and id
        result_label.configure(text=f"Student: {first_name} {last_name} with Student ID: {student_id} has been added.")
    
    #If an error occurs when entering the information into the database
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")
    
    #Finally exit the database
    finally:
        cursor.close()
        db.close()

########################################################################

#2. Function to Remove the course from the database
def removeCourse(course_id_entry, result_label):
    #Retrieve the user inputted information 
    course_id = course_id_entry.get()

    #Error to handle if the course id entry field is empty
    if not course_id:
        result_label.config(text="Course ID is required.")
        return

    #Connect to the database and try to remove the course
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to delete the course from the coures information
        cursor.execute("""
            DELETE FROM courseinformation WHERE CourseID = %s """, (course_id,))

        #Finializes the changest to the database
        db.commit()

        #If the course was removed return that it was completed
        if cursor.rowcount > 0:
            result_label.configure(text=f"Course ID: {course_id} has been removed.")
        else:
            #If the course cannot be found
            result_label.configure(text="Course not found.")

    #If an error occurs when removing the course from the database
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.config(text=f"Error: {sqlError}")

    #Finally exit the database
    finally:
        cursor.close()
        db.close()

#######################################################################

#3. Function to update the students information
def updateStudent(student_id_entry, first_name_entry, last_name_entry, major_entry, year_entry, GPA_entry, result_label):
    #Retrieve the user inputted information
    student_id = student_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    major = major_entry.get()
    year = year_entry.get()
    gpa = GPA_entry.get()

    #Error to handle if one of the entry fields are empty or NULL. All Entry fields must be filled.
    if not student_id or not first_name or not last_name or not major or not year or not gpa:
        result_label.config(text="All Entry fields are required.")
        return

    #Connect to the database and try to update the student information
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to update the students information
        cursor.execute("""
            UPDATE studentinformation 
            SET StuFirstName = %s, StuLastName = %s, Major = %s, Year = %s, GPA = %s
            WHERE StudentID = %s """, (first_name, last_name, major, year, gpa, student_id))

        #Finializes the changest to the database
        db.commit()

        #If the student ID does not exist in the database return that no student was found
        if cursor.rowcount == 0:
            result_label.configure(text="No student found with that ID.")
        
        #Return that the student information has been updated
        else:
            result_label.configure(text=f"{first_name} {last_name} with Student ID: {student_id} has been updated.")
    
    #If an error occurs when updating student information
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")
    
    #Finally exit the database
    finally:
        cursor.close()
        db.close()

####################################################################################

#4. Function to generate a report from high to low GPA's
def generateGPAReport(result_label):
    #Connect to the database and try to generate the gpa report
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to generate the GPA report from highest to lowest
        cursor.execute("""
            SELECT StudentID, StuFirstName, StuLastName, Major, Year, GPA 
            FROM studentinformation 
            ORDER BY GPA DESC """)

        #Retrieve the information for the GPA report
        students = cursor.fetchall()

        #Constructs the GPA report to be shown to the user
        report = "GPA Report Sorted by Highest to Lowest\n"
        report += "-" * 50 + "\n"
        for student in students:
            report += f"ID: {student[0]}, Name: {student[1]} {student[2]}, Major: {student[3]}, Year: {student[4]}, GPA: {student[5]}\n"

        #Returns the final GPA report to the user
        result_label.configure(text=report)

    #If an error occurs when generating the GPA report 
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")

    #Finally exit the database
    finally:
        cursor.close()
        db.close()

#####################################################################################################

#5. Function to remove a student from the database
def removeStudent(student_id_entry, result_label):
    #Retrieve the user inputted information 
    student_id = student_id_entry.get()

    #Error to handle if the student id entry field is empty
    if not student_id:
        result_label.config(text="Student ID is required.")
        return

    #Connect to the database and try to remove the student
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to delete the student from the coures information
        cursor.execute("""
            DELETE FROM studentinformation WHERE StudentID = %s """, (student_id,))

        #Finializes the changest to the database
        db.commit()

        #If the Student was removed return that it was completed
        if cursor.rowcount > 0:
            result_label.configure(text=f"Student ID: {student_id} has been removed.")
        else:
            #If the student cannot be found
            result_label.configure(text="Student not found.")

    #If an error occurs when removing the student from the database
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.config(text=f"Error: {sqlError}")

    #Finally exit the database
    finally:
        cursor.close()
        db.close()

##################################################################################################

#6. Function to Add a course to the database
def addCourse(course_id_entry, course_name_entry, course_code_entry, department_id_entry, credit_hours_entry, instructor_id_entry, result_label):
    #Retrieve the user inputted information 
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()
    course_code = course_code_entry.get()
    department_id = department_id_entry.get()
    credit_hours = credit_hours_entry.get()
    instructor_id = instructor_id_entry.get()

    #Error to handle if one of the entry fields are empty or NULL. All Entry fields must be filled.
    if not course_id or not course_name or not course_code or not department_id:
        result_label.config(text="All Entry fields are required.")
        return

    #Connect to the database and try to add the course
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to insert the student into the database
        cursor.execute(""" 
            INSERT INTO courseinformation (CourseID, CourseName, CourseCode, DepartmentID, CreditHours, InstructorID) 
            VALUES (%s, %s, %s, %s, %s, %s)""", (course_id, course_name, course_code, department_id, credit_hours, instructor_id))

        #Finializes the changes to the database
        db.commit()

        #Returns that it was complete, with the course name, code, and id
        result_label.configure(text=f"Course: {course_name} {course_code} with Course ID: {course_id} has been added.")
    
    #If an error occurs when entering the course information into the database
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")
    
    #Finally exit the database
    finally:
        cursor.close()
        db.close()
        
###################################################################################################################

#7. Function to generate a courses report
def generateCourseReport(result_label):
    #Connect to the database and try to generate the course report
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to generate the course report
        cursor.execute("""
            SELECT CourseName, CourseCode, CreditHours
            FROM courseinformation """)

        #Retrieve the information for the course report
        courses = cursor.fetchall()

        #Constructs the course report to be shown to the user
        report = "Course Report\n"
        report += "-" * 50 + "\n"
        for course in courses:
            report += f"Course Name: {course[0]} {course[1]}, Credit Hours: {course[2]}\n"

        #Returns the final course report to the user
        result_label.configure(text=report)

    #If an error occurs when generating the course report 
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")

    #Finally exit the database
    finally:
        cursor.close()
        db.close()

########################################################################################################

#8. Function to generate a report of students enrolled in a specific course
def generateEnrolledCourseReport(course_id_entry, result_label):
    #Retrieve the user inputted information 
    course_id = course_id_entry.get()

    #Error to handle if one of the entry fields are empty or NULL. All Entry fields must be filled.
    if not course_id:
        result_label.config(text="Course ID Entry field is required.")
        return

    #Connect to the database and try to generate the enrolled course report
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to generate the enrolled course report
        cursor.execute("""
            SELECT s.StudentID, s.StuFirstName, s.StuLastName, c.CourseName, c.CourseCode
            FROM studentinformation s
            JOIN studentenrollment se ON s.StudentID = se.StudentID
            JOIN courseinformation c ON se.CourseID = c.CourseID
            WHERE c.CourseID = %s """, (course_id,))

        #Retrieve the information for the course report
        students = cursor.fetchall()

        #Constructs the course report to be shown to the user
        if students:
            report = f"Course Enrollment Report for Course ID {course_id}\n"
            report += "-" * 50 + "\n"
            for student in students:
                report += f"Student ID: {student[0]}, Student Name: {student[1]} {student[2]}, Course: {student[3]} {student[4]}\n"
        #If there are no students in the course return that no students enrolled
        else:
            report = f"No students are enrolled in this course, Course ID: {course_id}."

        #Returns the final enrolled course report to the user or that no students are enrolled in that course
        result_label.configure(text=report)

    #If an error occurs when generating the enrolled course report
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")

    #Finally exit the database
    finally:
        cursor.close()
        db.close()

##############################################################################################################

#9. Function to generate a report of a specific students information
def generateStudentInformationReport(student_id_entry, result_label):
    #Retrieve the user inputted information 
    student_id = student_id_entry.get()

    #Error to handle if one of the entry fields are empty or NULL. All Entry fields must be filled.
    if not student_id:
        result_label.config(text="Student ID Entry field is required.")
        return

    #Connect to the database and try to generate the enrolled course report
    try:
        db = connect_to_database()
        cursor = db.cursor()

        #The SQL to generate the enrolled course report
        cursor.execute("""
            SELECT 
                s.StudentID, 
                s.StuFirstName, 
                s.StuLastName, 
                s.Major, 
                s.Year, 
                s.GPA, 
                h.HousingStatus, 
                h.Building, 
                f.PaymentStatus, 
                f.AmountDue, 
                c.PhoneNumber, 
                c.EmailAddress, 
                GROUP_CONCAT(DISTINCT co.CourseName ORDER BY co.CourseID) AS EnrolledCourses, 
                GROUP_CONCAT(DISTINCT co.CourseCode ORDER BY co.CourseID) AS CourseCodes 
            FROM 
                studentinformation s 
            LEFT JOIN 
                housingstatus h ON s.StudentID = h.StudentID 
            LEFT JOIN 
                financialaid f ON s.StudentID = f.StudentID 
            LEFT JOIN 
                studentcontact c ON s.StudentID = c.StudentID 
            LEFT JOIN 
            studentenrollment se ON s.StudentID = se.StudentID 
            LEFT JOIN 
                courseinformation co ON se.CourseID = co.CourseID 
            WHERE s.StudentID = %s
            GROUP BY s.StudentID, s.StuFirstName, s.StuLastName, s.Major, s.Year, s.GPA, h.HousingStatus, 
            h.Building, f.PaymentStatus, f.AmountDue, c.PhoneNumber, c.EmailAddress """, (student_id,))

        #Retrieve the information for the student information report
        students = cursor.fetchone()

        #Constructs the student information report to be shown to the user
        if students:
            report = f"Student Information Report for Student ID {student_id}\n"
            report += "-" * 50 + "\n"
            report += f"Student Name: {students[1]} {students[2]}\n"
            report += f"Major: {students[3]}, Year: {students[4]}, GPA: {students[5]}\n"
            report += f"Housing Status: {students[6]} - {students[7]}\n"
            report += f"Payment Status: {students[8]}, Amount Due: ${students[9]:.2f}\n"
            report += f"Contact Information: {students[10]}, {students[11]}\n"
            report += f"Enrolled Courses: {students[12] if students[12] else 'No courses enrolled'}\n"
            report += f"Course Codes: {students[13] if students[13] else 'No courses enrolled'}\n"

        #If there are no students with that student id
        else:
            report = f"There exists no Student by Student ID: {student_id}."

        #Returns the final student information report to the user or that no such student exists
        result_label.configure(text=report)

    #If an error occurs when generating the student information report
    except mysql.connector.Error as sqlError:
        #Return the error to the user
        result_label.configure(text=f"Error: {sqlError}")

    #Finally exit the database
    finally:
        cursor.close()
        db.close()

#Runs the App
app = App()
app.mainloop()