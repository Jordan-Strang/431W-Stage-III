import tkinter
import customtkinter
import mysql.connector

#Connect to the locally hosted database
def connect_to_database():
    """Function to connect to the database"""
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
        result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 12, "italic"))
        result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        #A button to add the student information from the entered fields
        add_button = customtkinter.CTkButton(self, text="Add Student", command=lambda: addStudent(student_id_entry, first_name_entry, last_name_entry, major_entry, year_entry, GPA_entry, result_label), font=("Arial", 12, "bold"), corner_radius=8, hover_color="lightblue")
        add_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
     
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

    #Error to handle if one of the fields are empty or NULL. All Entry fields must be filled.
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


#Runs the App
app = App()
app.mainloop()
