#Tkinter is a standard Python GUI library that provides tools and widgets for creating desktop applications with graphical interfaces.
import tkinter as tk

#Create a calculation string which will be empty at first
calculation = ""

def addToCalculation(symbol):
    #Make calculation a global variable so that we can manipulate it inside the function
    global calculation
    #Type cast symbol into a string regardless of its actual type
    calculation += str(symbol)
    
    text_result.delete(1.0, "end") # 1.0 is the starting index and end is the ending index, that way all the content currently in the text field is deleted
    text_result.insert(1.0, calculation)

#Function to call eval() and then do the necessary tkinter operations
def evaluateCalculation():
    #REMEMBER TO BE CAUTIOUS WHEN USING THE eval() function, since it evaluates code as well
    
    global calculation
    
    try:
        calculation = str(eval(calculation))

        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        
    except:
        clearField()
        text_result.insert(1.0, "Error")

def clearField():
    global calculation
    calculation = ""
    
    text_result.delete(1.0, "end")


#Build a basic window or GUI that will say we want to have a text field and we want to get values from it, clear it etc

#Create window
root = tk.Tk()

#Define dimensions of the window
root.geometry("500x400")

#Text field for results
text_result = tk.Text(root, height=2, width=25, font=("Arial", 24))
text_result.grid(columnspan=5) #columnspan=5 means the text field should go across all the specified 5 colums

#Create individual buttons
btn1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), width=5, font=("Arial", 14))
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), width=5, font=("Arial", 14))
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), width=5, font=("Arial", 14))
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), width=5, font=("Arial", 14))
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), width=5, font=("Arial", 14))
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), width=5, font=("Arial", 14))
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), width=5, font=("Arial", 14))
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), width=5, font=("Arial", 14))
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), width=5, font=("Arial", 14))
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), width=5, font=("Arial", 14))
btn0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: addToCalculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: addToCalculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_times = tk.Button(root, text="*", command=lambda: addToCalculation("*"), width=5, font=("Arial", 14))
btn_times.grid(row=4, column=4)

btn_divide = tk.Button(root, text="/", command=lambda: addToCalculation("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: addToCalculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: addToCalculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluateCalculation, width=15, font=("Arial", 14))
btn_equals.grid(row=6, column=1, columnspan=2)

btn_clear = tk.Button(root, text="C", command=clearField, width=9, font=("Arial", 14))
btn_clear.grid(row=6, column=4, columnspan=2)

#Endpoint
root.mainloop()
