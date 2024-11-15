import tkinter as tk

class PasswordGui:
    def __init__(self):
        #tkintr dimensions and label
        self.window = tk.Tk()
        self.window.title('Passwords')
        self.window.geometry('500x500')

        self.window.grid_columnconfigure(0, weight=10)
        self.window.grid_rowconfigure(1, weight=10)

        #text/display area
        self.text_area = tk.Text(self.window,padx=5,pady=5)
        self.text_area.grid()

        #create a button frame
        self.button_frame = tk.Frame(self.window)
        self.button_frame.grid(row=1,column=0)
        self.initialize_button = tk.Button(self.button_frame,text='Initialize')
        self.generate_pass = tk.Button(self.button_frame,text="Generate Password")
        self.initialize_button.pack(side='left',padx=30)
        self.generate_pass.pack(side='right',padx=30)


    
    def run (self):
        self.window.mainloop()

        
a = PasswordGui() 
a.run()     
