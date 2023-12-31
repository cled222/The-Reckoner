
from tkinter import *
from final_button_data import button_data

WIDTH = 400
HEIGHT = 650


class MainGUI(Frame):
    rows = 6
    columns = 4
    def __init__(self,parent):
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)     how to make it fullscreen
        self.setupGUI()
        self.solution = False       #new boolean value that determines if value is a solution
    
    def setupGUI(self):
        #the display
        self.display = Label(
            self,           #MainGUI class is the parent of this label
            text = "",
            anchor = E,
            bg = "white",
            fg= "black",
            borderwidth=1,
            height =1, 
            font = ("TexGyreAdventor", 45)      #sets font with tuple(font name, size)
        )
        
        self.display.grid(row=0, column = 0, columnspan = 4, sticky = NSEW)
        
        #configuring grid, allows rows and columns to expand with window
        for row in range(MainGUI.rows):
            Grid.rowconfigure(self, row, weight=1)
            
        for column in range(MainGUI.columns):
            Grid.columnconfigure(self, column, weight=1)
            
        
        #create buttons
        for button in button_data:          #calls upon dictionary keys
            self.make_button(button["row"], button["col"], button["value"], button["columnspan"]) 
        
        #pack
        self.pack(fill=BOTH, expand=1)
        
    
    def make_button(self, row, col, value, span):
        bg_color = "#dddddd"
        if value== "=":
            bg_color = "blue"
        if value in ['(',')', 'AC', '**', '+', '-', '*', '/','%','←']:
            bg_color = "#999999"
                
        button = Button(
            self,
            font = ("TexGyreAdventor", 30),
            text = value,
            fg = "black",
            bg = bg_color,#windows
            highlightbackground = bg_color,#mac
            borderwidth=1,
            highlightthickness=0,
            width=5,
            activebackground = "white",
            command= lambda: self.process(value)    #wraps a function when using it as a definition (not actually running it)
        )
        button.grid(row=row, column=col, columnspan = span, sticky=NSEW)
    
    def clear_display(self):
        self.display["text"] = ""
        
    def delete_character(self):                 #added for the <-- button
        expression = self.display["text"]
        result = expression[:-1]
        self.set_display(result)
        
        
    def set_display(self, value):
        self.display["text"] = value
        
    def append_display(self,value):         #I set restrictions in order to clear the previous display when an error was reached
        expression = self.display["text"]
        if len(expression) > 13:
            self.clear_display()
            self.display["text"] += "Error:val!>14"
        elif expression == "ERROR":
            self.clear_display()
            self.display["text"] += value
        elif expression == "Error:val!>14":
            self.clear_display()
            self.display["text"] += value
        else:
            self.display["text"] += value
        
    def evaluate (self):                    #this function ensures that solutions of over 14 character are returned as "{11 characters}..."
        expression = self.display["text"]
        try:
            #do this until it hits an error
            result = str(eval(expression))
            if len(result) > 14:
                result = f"{result[0:11]}..."
            self.set_display(result)
                
        except:                
            #if error reached, do this...
             self.set_display("ERROR")

            
    
    def process(self, button_):  #I added more elifs for the new buttons and a variable to determine if a solution is reached
                                 #allowing me to clear it for the new appended value
        if button_ == "AC":
            #clear the display
            self.clear_display()
            
        elif button_ == "=":
        #evaluate expression in the display
            self.solution = True
            self.evaluate()
        elif button_ == "%":
            self.append_display(button_)
        elif button_ == '←':
            self.delete_character()
        else:
            #append to display
            if self.solution == True:
                self.clear_display()
                self.solution = False
                self.append_display(button_)
            else:
                self.append_display(button_)

#main
window = Tk()
window.title("The Reckoner")
window.geometry(f"{WIDTH}x{HEIGHT}")
p = MainGUI(window)
window.mainloop()
