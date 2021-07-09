from tkinter import *
from math import *
class Calculator:
    def __init__(self):
        # append the inputs to the list
        self.list_1 = []
        window = Tk()
        window.title("Calculator")
        menu_bar = Menu(window) 
        window.config(menu = menu_bar) # Display menu bar
        
        # Create pull down menu and add to the menu bar
        mode_menu = Menu(menu_bar, tearoff = 0) # tearoff is used to prevent the menu from being removed
        menu_bar.add_cascade(label = "Mode", menu = mode_menu)
        mode_menu.add_command(label = "Comp", command = self.Comp) # the command Comp is the normal settings of a calculator
        mode_menu.add_command(label = "Equation", command = self.Equation) # the command Equation is the equation mode 
        
        #create frames
        frame_1 = Frame(window)
        frame_2 = Frame(window)
        frame_3 = Frame(window)
        frame_4 = Frame(window)
        frame_5 = Frame(window)
        frame_6 = Frame(window)
        frame_7 = Frame(window)
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        frame_5.pack()
        frame_6.pack()
        frame_7.pack()
        
        # create entry
        self.input_1 = StringVar()
        self.entry_1 = Entry(frame_1, textvariable = self.input_1, font = "Arial 40 bold", width = 50)
        self.result = StringVar()
        self.entry_2 = Label(frame_2, textvariable = self.result, font = "Arial 40 bold", bg = "white", width = 42, justify = LEFT)
        
        self.entry_1.grid(row = 1, column = 1)
        self.entry_2.grid(row = 2, column = 1, sticky = E)
        
        # create the calculator buttons
        button_AC = Button(frame_3, text = "AC", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.AC)   
        
        button_7 = Button(frame_4, text = "7", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(7))
        button_8 = Button(frame_4, text = "8", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(8))
        button_9 = Button(frame_4, text = "9", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(9))
        button_open_bracket = Button(frame_4, text = "(", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('('))
        button_close_bracket = Button(frame_4, text = ")", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(')'))
        button_sin = Button(frame_4, text = "sin", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('sin('))
        button_sin_inverse = Button(frame_4, text = "asin", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('asin('))
        
        button_4 = Button(frame_5, text = "4", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(4))
        button_5 = Button(frame_5, text = "5", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(5))
        button_6 = Button(frame_5, text = "6", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(6))
        button_multiplication = Button(frame_5, text = "X", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('*'))
        button_division = Button(frame_5, text = "/", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('/'))
        button_cos = Button(frame_5, text = "cos", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('cos('))
        button_cos_inverse = Button(frame_5, text = "acos", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('acos('))
        
        button_1 = Button(frame_6, text = "1", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(1))
        button_2 = Button(frame_6, text = "2", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(2))
        button_3 = Button(frame_6, text = "3", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(3))
        button_subtraction = Button(frame_6, text = "-", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('-'))
        button_addition = Button(frame_6, text = "+", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('+'))
        button_tan = Button(frame_6, text = "tan", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('tan('))
        button_tan_inverse = Button(frame_6, text = "atan", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('atan('))     
        
        button_0 = Button(frame_7, text = "0", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons(0))
        button_decimal_point = Button(frame_7, text = ".", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('.'))
        button_del = Button(frame_7, text = "Del", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.Del)
        button_equal = Button(frame_7, text = "=", width = 12, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.answer)
        button_log = Button(frame_7, text = "ln", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('ln('))
        button_log_inverse = Button(frame_7, text = "ln-1", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = lambda: self.buttons('ln-1('))        
        
        
        # Arrange the buttons 

        button_AC.grid(row = 3, column = 1, sticky = W)
        
        button_7.grid(row = 5, column = 1, sticky = W, ipadx = 10, ipady= 10)
        button_8.grid(row = 5, column = 2, sticky = W, ipadx = 10, ipady= 10)
        button_9.grid(row = 5, column = 3, sticky = W, ipadx = 10, ipady= 10)
        button_open_bracket.grid(row = 5, sticky = W, column = 4, ipadx = 10, ipady = 10)
        button_close_bracket.grid(row = 5, column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_sin.grid(row = 5, column = 6, sticky = W, ipadx = 10, ipady = 10)
        button_sin_inverse.grid(row = 5, column = 7, sticky = W, ipadx = 10, ipady = 10)
        
        button_4.grid(row = 6, column = 1, sticky = W, ipadx = 10, ipady= 10)
        button_5.grid(row = 6, column = 2, sticky = W, ipadx = 10, ipady= 10)
        button_6.grid(row = 6, column = 3, sticky = W, ipadx = 10, ipady= 10)
        button_multiplication.grid(row = 6, column = 4, sticky = W, ipadx = 10, ipady= 10)
        button_division.grid(row = 6, column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_cos.grid(row = 6, column = 6, sticky = W, ipadx = 10, ipady = 10)
        button_cos_inverse.grid(row = 6, column = 7, sticky = W, ipadx = 10, ipady = 10)
        
        button_1.grid(row = 7, column = 1, sticky = W, ipadx = 10, ipady= 10)
        button_2.grid(row = 7, column = 2, sticky = W, ipadx = 10, ipady= 10)
        button_3.grid(row = 7, column = 3, sticky = W, ipadx = 10, ipady= 10)
        button_subtraction.grid(row = 7, column = 4, sticky = W, ipadx = 10, ipady = 10)
        button_addition.grid(row = 7 , column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_tan.grid(row = 7, column = 6, sticky = W, ipadx = 10, ipady = 10)
        button_tan_inverse.grid(row = 7, column = 7, sticky = W, ipadx = 10, ipady = 10)        
        
        button_0.grid(row = 8, column = 1, sticky = W, ipadx = 10, ipady = 10)
        button_decimal_point.grid(row = 8, column = 2, sticky = W, ipadx = 10, ipady = 10)
        button_del.grid(row = 8, column = 3, sticky = W, ipadx = 10, ipady = 10)
        button_equal.grid(row = 8, column = 4, sticky = W, ipadx = 10, ipady = 10)
        button_log.grid(row = 8, column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_log_inverse.grid(row = 8, column = 6, sticky = W, ipadx = 10, ipady = 10)         
        
        window.mainloop()
        
        
    def Comp(self):
        pass
    def Equation(self):
        pass
    def buttons(self, button):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(button)
            
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.insert(self.entry_1.index(INSERT), button)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), button)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)       
        
    def AC(self):
        self.entry_1.delete(0, END) # delete everything inputed in the entry from the first index to the last index 
        # or
        # self.result.set("")
        
        # Working with lists therefore need to clear the list for the AC button to work properly if this is not done even after using the AC button 
        # once any other entry button is clicked the whole previously entered data will reappear
        self.list_1.clear()
        
    def Del(self):
        if self.entry_1.index(INSERT) == 0:
            self.list_1.pop()
        # removing the last data in the list 
        # del what is before the cursor
        else:
            self.list_1.remove(self.list_1[self.entry_1.index(INSERT) -1 ])
            # to make the cursor move when the character is deleted
            self.entry_1.icursor(self.entry_1.index(INSERT) - 1)
        
        # showing the list_1 in the entry
        self.input_1.set(self.list_1)
        
        
        # prevent the entry from scattering when the del button is pressed
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the  input to the processed form
        self.input_1.set(processed_form)         
    
    
    
    # process the input
    def process_input(self):
        # since list is used to store the inputs this is to prevent the result from giving the exact same input
        processed_form_list = []
        processed_form = ''
        # for element in self.list_1.index("tan(")
        # create a new list that we can manipulate but will not display on the entry
        for element in self.list_1:
            processed_form_list.append(element)
            # since python by default takes the argument in tan() to be in radians this changes is to degrees
            if 'tan(' in processed_form_list:
                processed_form_list[processed_form_list.index('tan(')] = 'tan(float(pi/180)*'
            if 'sin(' in processed_form_list:
                processed_form_list[processed_form_list.index('sin(')] = 'sin(float(pi/180)*'
            if 'cos(' in processed_form_list:
                processed_form_list[processed_form_list.index('cos(')] = 'cos(float(pi/180)*'
            if 'atan(' in processed_form_list:
                processed_form_list[processed_form_list.index('atan(')] = '(180/pi)*atan('
            if 'asin(' in processed_form_list:
                processed_form_list[processed_form_list.index('asin(')] = '(180/pi)*asin('
            if 'acos(' in processed_form_list:
                processed_form_list[processed_form_list.index('acos(')] = '(180/pi)*acos('
            if 'ln-1(' in processed_form_list:
                processed_form_list[processed_form_list.index('ln-1(')] = 'e**('
            
        for chars in processed_form_list:
            processed_form += str(chars)
        
        
        try:
            answer = eval(processed_form)
            return answer
        except:
            return "Error"
    def answer(self):
        self.result.set((self.process_input()))
    
Calculator()

# How to handle sin to give answer as a calculator in degrees mode
# to get answer of sin inverse in degrees
# print(asin(1) * 180/pi)
""" identifing where the cursor is in the entry 
window = Tk()
entry_1 = Entry(window)
entry_1.pack()
print(entry_1.index(INSERT))
window.mainloop()"""