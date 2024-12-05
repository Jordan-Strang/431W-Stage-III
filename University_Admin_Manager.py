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


#Runs the App
app = App()
app.mainloop()
