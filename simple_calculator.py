# A tkinter-based user interface of a simple calculator which can handle
# simple calculation including:
#   - multiply *
#   - divide /
#   - add +
#   - substract -
#   - square root √



from tkinter import *
from math import *


DEFAULT_FONT = ('Arial', 20)
expression = ""


def button_pressed(num) -> None:
    '''
    A function to update expression in the text label entry
    '''
    global expression
    expression = expression + str(num)
    equation.set(expression)
    

def square_root_pressed() -> None:
    '''
    - Function to evaluate the square root of a number or an expression
    - Enter a number or an expression and then press '√' button would
    display the result
    - Handling case when pressing '√' button before pressing a number 
    '''
    try:
        global expression
        result = str(eval('sqrt(' + expression + ')'))
        equation.set(result)
        expression = ""
    except TypeError:
        equation.set("Enter a number first")
        expression = ""
    
    
def equal_pressed() -> None:
    '''
    - A function to evaluate the final expression and display result
    on text label entry once pressing the '=' button 
    - Handling zero division 
    '''
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except ZeroDivisionError:
        equation.set("Error: Divide by 0")
        expression = ""


def clear()-> None:
    '''
    A function to clear text label entry when pressing 'Clear' button
    '''
    global expression
    expression = ""
    equation.set(expression)

    
def display():
    '''
    A function to build the GUI for the calculator, it consists of
    a label text exntry in the top row spanning from column 0 to 4,
    and then rows and columns of the calculator's buttons.
    '''
    # create a text label entry to display expression and result
    display_label = Label(
        root, textvariable = equation, font = DEFAULT_FONT, 
        bg = "#deebf7", fg = "#3182bd", anchor = "e")
    display_label.grid(
        row = 0, column = 0, columnspan = 4, sticky = "nsew")
    display_label.bind('<Enter>', on_mouse_entered_button)
    display_label.bind('<Leave>', on_mouse_exited_button)

    # create buttons and place inside the root window,
    # command and function are bound to each button
    button_sqrt = Button(
        root, text = "√", font = DEFAULT_FONT,
        bg = "#deebf7", fg = "#3182bd",
        relief = RIDGE,
        command=square_root_pressed)
    button_sqrt.grid(
        row = 1, column = 0, columnspan = 3, sticky = "nswe")
    button_sqrt.bind('<Enter>', on_mouse_entered_button)
    button_sqrt.bind('<Leave>', on_mouse_exited_button)
    
    button_divide = create_button(
        root, '/', 1, 3,
        command=lambda: button_pressed("/"))
    
    button_7 = create_button(
        root, '7', 2, 0,
        command=lambda: button_pressed("7"))
    button_8 = create_button(
        root, '8', 2, 1,
        command=lambda: button_pressed("8"))
    button_9 = create_button(
        root, '9', 2, 2,
        command=lambda: button_pressed("9"))
    button_multiply = create_button(
        root, 'x', 2, 3,
        command=lambda: button_pressed("*"))
    
    button_4 = create_button(
        root, '4', 3, 0,
        command=lambda: button_pressed("4"))
    button_5 = create_button(
        root, '5', 3, 1,
        command=lambda: button_pressed("5"))
    button_6 = create_button(
        root, '6', 3, 2,
        command=lambda: button_pressed("6"))
    button_subtract = create_button(
        root, '–', 3, 3,
        command=lambda: button_pressed("-"))
    
    button_1 = create_button(
        root, '1', 4, 0,
        command=lambda: button_pressed("1"))
    button_2 = create_button(
        root, '2', 4, 1,
        command=lambda: button_pressed("2"))
    button_3 = create_button(
        root, '3', 4, 2,
        command=lambda: button_pressed("3"))
    button_plus = create_button(
        root, '+', 4, 3,
        command=lambda: button_pressed("+"))
    
    button_clear = Button(
        root, text = 'Clear', font = DEFAULT_FONT,
        bg = "#deebf7", fg = "#3182bd",
        relief = RIDGE,
        command=clear)
    button_clear.grid(
        row = 5, column = 0, columnspan = 2, sticky = "nswe")
    button_clear.bind('<Enter>', on_mouse_entered_button)
    button_clear.bind('<Leave>', on_mouse_exited_button)
    button_0 = create_button(
        root, '0', 5, 2,
        command=lambda: button_pressed("0"))
    
    button_equal = create_button(
        root, '=', 5, 3,
        command=equal_pressed)
    
    # rows and columns of the grid change proportionately as
    # the size of the root window changes
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 1)
    root.rowconfigure(3, weight = 1)
    root.rowconfigure(4, weight = 1)
    root.rowconfigure(5, weight = 1)

    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)
    root.columnconfigure(2, weight = 1)
    root.columnconfigure(3, weight = 1)
    
    root.mainloop()
    

def create_button(root, text, row, column, command) -> Button:
    '''
    A function to create button by specifying text displayed,
    row, column on the root window and command affiliated with that button 
    Return a Button 
    '''
    button = Button(
        root, text = text, font = DEFAULT_FONT,
        bg = "#deebf7", fg = "#3182bd",
        relief = RIDGE, command=command)
    button.grid(
        row = row, column = column, sticky = "nswe")
    # binding the event handler function with each button to increase/
    # decrease its font size on mouse entered or exited button
    button.bind('<Enter>', on_mouse_entered_button)
    button.bind('<Leave>', on_mouse_exited_button)

    return button


def on_mouse_entered_button(event) -> None:
    '''
    Event handler function called when the mouse enters a single button.
    Accessing button's options, in this case we want to set
    the 'font' option of a button, in particular increasing the font's
    size of the button.
    '''
    event.widget['font'] = ('Arial', 45, 'bold')


def on_mouse_exited_button(event) -> None:
    '''
    Event handler function called when the mouse exits a single button.
    Accessing button's options, in this case we want to set
    the 'font' option of a button back to default size.
    '''
    event.widget['font'] = DEFAULT_FONT


if __name__ == "__main__":
    # create a Tk root window
    root = Tk()
    root.title("Simple Calculator")
    # set default configuration for the root window
    root.geometry("300x400")
    # create a variable of StringVar class
    equation = StringVar()
    display()

    
    
    
