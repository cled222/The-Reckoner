#Name: Caiden Ledet
#Date:2/3/23
#Description: The reckoner calculator

from tkinter import *
from button_data import button_data

WIDTH = 400
HEIGHT = 650


class MainGUI(Frame):
    rows = 6
    columns = 4
    def __init__(self,parent):
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)     how to make it fullscreen
        self.setupGUI()
    
    def setupGUI(self):
        #the display
        self.display = Label(
            self,           #MainGUI class is the parent of this label
            text = "",
            anchor = E,
            bg = "white",
            fg= "black",
            height =1, 
            font = ("TexGyreAdventor", 50)      #sets font with tuple(font name, size)
        )
        
        self.display.grid(row=0, column = 0, columnspan = 4, sticky = NSEW)
        
        #configuring grid, allows rows and columns to expand with window
        for row in range(MainGUI.rows):
            Grid.rowconfigure(self, row, weight=1)
            
        for column in range(MainGUI.columns):
            Grid.columnconfigure(self, column, weight=1)
            
        
        #create buttons
        for button in button_data:          #calls upon dictionary keys
            self.make_button(button["row"], button["col"], button["value"])
        
        #pack
        self.pack(fill=BOTH, expand=1)
        
    
    def make_button(self, row, col, value):
        bg_color = "#dddddd"
        if value== "=":
            bg_color = "blue"
        if value in ['(',')', 'AC', '**', '+', '-', '*', '/']:
            bg_color = "#999999"
                
        button = Button(
            self,
            font = ("TexGyreAdventor", 30),
            text = value,
            fg = "black",
            bg = bg_color,#windows
            highlightbackground = bg_color,#mac
            borderwidth=0,
            highlightthickness=0,
            width=5,
            activebackgroun = "white",
            command= lambda: self.process(value)    #wraps a function when using it as a definition (not actually running it)
        )
        button.grid(row=row, column=col, sticky=NSEW)
    
    def clear_display(self):
        self.display["text"] = ""
        
    def set_display(self, value):
        self.display["text"] = value
        
    def append_display(self,value):
        self.display["text"] += value
        
    def evaluate (self):
        expression = self.display["text"]
        try:
            #do this until it hits an error
            result = str(eval(expression))
            self.set_display(result)
                
        except:                
            #if error reached, do this...
             self.set_display("ERROR")
            
    
    def process(self, button_):
        if button_ == "AC":
            #clear the display
            self.clear_display()
            
        elif button_ == "=":
        #evaluate expression in the display
            self.evaluate()
        else:
            #append to display
            self.append_display(button_)

#main
window = Tk()
window.title("The Reckoner")
window.geometry(f"{WIDTH}x{HEIGHT}")
p = MainGUI(window)
window.mainloop()





#ANother way to define lambda functions
#my_function = lambda x: x+2

#my_function(3)
