import tkinter as tk
import sys
import subprocess
import ctypes

class PasswordGui:
    def __init__(self):
        #tkintr dimensions and label
        self.window = tk.Tk()
        self.window.title('Passwords')
        self.window.geometry('500x500')

        self.window.grid_columnconfigure(0, weight=10)
        self.window.grid_rowconfigure(1, weight=10)

        #text/display area
        self.text_area = tk.Text(self.window)
        self.text_area.pack(fill=tk.BOTH, expand=True,padx=5,pady=5)

        #create a button frame
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(fill=tk.X, pady=10)

        #create buttons
        self.initialize_button = tk.Button(self.button_frame,text='Initialize',command=self.initialize)
        self.generate_pass = tk.Button(self.button_frame,text="Generate Password",command=self.generatePass)
        self.initialize_button.pack(side='left',padx=5)
        self.generate_pass.pack(side='right',padx=5)

    def is_admin(self):
        #Check if the script is running with admin privileges.
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def initialize(self):
        #This is the intialize button, it helps to provide admin access level to the script, it should only be used once per script
        self.text_area.delete('1.0',tk.END)
        if not self.is_admin():
            # Relaunch the script with admin privileges
            self.text_area.insert('1.0',"Relaunching with administrative privileges...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            # Run the function as an admin
            self.generatePass()

            
    def generatePass(self):
        #logic for the display and obtaining the wifi-passwords
        self.text_area.delete('1.0',tk.END)
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], text=True)
        profiles = [content.strip().split(':')[1].strip() for content in result.splitlines() if 'All User Profile' in content]
        wifi_data = {}
    
        for profile in profiles:
            try:
                data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear'],text=True)
                pass_ = [content.split(':')[1].strip() for content in data.splitlines() if 'Key Content' in content]
                wifi_data[profile] = pass_
            except subprocess.CalledProcessError as e:
                self.text_area('1.0',f'Error fetching data for {profile}: {e}')
    
        for key,value in wifi_data.items():
            self.text_area.insert('1.0',f'{key}\t\t{value}')
    
    def run (self):
        self.window.mainloop()

if __name__ == '__main__':      
    a = PasswordGui() 
    a.run()     
