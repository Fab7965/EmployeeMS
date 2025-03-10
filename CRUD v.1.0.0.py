##as a note, messages that start with 2 hashtags have been added later on in the process
##for workflow purposes ie, creating new functions after I designed a button calling it.
#create a CRUD app that can;
#insert and store employee details such as Employee ID, Name, and Department
#fetch, delete, and update data.
#Show all data available in the database
#And Has a simple GUI interface to perform all the operations listed above.
#Importing the modules I need
import mysql.connector
myDB = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "Potato3", 
database = "employee")
myCur = myDB.cursor()
from tkinter import*

window = Tk()
##adding the messagebox submodule from tinker it has to be a seperate line as
##"*" only imports core widgets and functions.
from tkinter import messagebox
#Creating the GUI

#The GUI will need a Label to describe the input fields,
#Buttons to activate the commands, an entry module to accept inputs,
#a listbox to display the data, and a Parent window to hold it all.
#setting the size of the window 
window.geometry("600x270")
window.title("Employee CRUD App")


#adding Label and Entry Widgets
empID = Label(window, text="Employee ID", font=("Serif", 12))
empID.place(x=20, y=30)

empName = Label(window, text="Employee Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Serif",12))
empDept.place(x=20, y=90)

enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)
##Creating the functions that interact with the database

def insertData():
    #Read data provided by user.
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()
    if(id == "" or name == "" or dept ==""):
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
    else:#Insert data in the empDetails table
        insSql= "INSERT INTO empDetails (empId, empName, empDept) VALUES (%s, %s, %s)"
        insVal=(id, name, dept)
        myCur.execute(insSql, insVal)
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        ###call the show function to update the widget
        show()
        messagebox.showinfo("Insert Status", "Data Inserted Sucessfully")
def updateData():
    #read input data
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()
    if(id == ""):
        messagebox.showwarning("Cannot Update", "id Field Required!!!")
    else: #update empDetails table
        updSql= "UPDATE empDetails SET empName = %s, empDept = %s WHERE empID = %s"
        updVal=(name, dept, id)
        myCur.execute(updSql, updVal)
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        show()
        messagebox.showinfo("Update Status", "Data Updated Sucessfully")

def getData():
    id = enterId.get()
    if(id == ""):
       messagebox.showwarning("Fetch Status", "Please provide the Emp ID to fetch the data")
    else:
        fetSql= "SELECT * FROM empDetails WHERE empID = %s"
        fetVal= (id,)# Create a tuple with the id_value as sql expects a list not a string in order to process it in this context.
        myCur.execute(fetSql, fetVal)
        rows= myCur.fetchall()

        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])
def deleteData():
    id = enterId.get()
    if(id == ""):
       messagebox.showwarning("Cannot Delete", "Please provide the Emp ID to delete the corresponding data")
    else:
        delSql= "DELETE FROM empDetails WHERE empID = %s"
        delVal=(id,)
        myCur.execute(delSql, delVal)
        myDB.commit()
        # Clear out data from all fields
        enterId.delete(0, "end")
        enterName.delete(0,"end")
        enterDept.delete(0, "end")
        show()
        messagebox.showinfo("Delete Status","Data Deleted Successfully")
def potato():
    pass
def show():
    myCur.execute("SELECT * FROM empDetails")
    rows = myCur.fetchall()
#empty the list before doing anything to ensure no duplicate or outdated data accumulates.
    showData.delete(0, showData.size())
    for row in rows:
        addData = str(row[0]) + " " + row[1]+ " " + row[2]
        showData.insert(showData.size() + 1, addData)
def resetFields():
    enterId.delete(0,"end")
    enterName.delete(0, "end")
    enterDept.delete(0,"end")
#Adding the buttons, however in order to test it I cannot give them any functionality instead using the pass function
insertBtn = Button(window, text="Insert", font=("Sans", 12), bg="white",
command=insertData)
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text="Update", font=("Sans", 12), bg="white"
,command=updateData)
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font = ("Sans", 12), bg="white",
command=getData)
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=("Sans", 12), bg="white",
command=deleteData)
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=("Sans", 12), bg="white",
command=resetFields)
resetBtn.place(x=20, y=210)
#Adding the Listbox
showData = Listbox(window)
showData.place(x=330, y=30)
###added call to show the data in listbox when it's created
show()
window.mainloop()
#Challenge. implement the other 2 projects with a gui, Implement Exception handling into all of them.