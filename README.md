### wifipasswordGUI
Creating a GUI pragram that displays all saved wifi password on the current system.
Windows OS only
This script attempts to restart itself with admin privileges using ctypes. However, if some system blocks this or has restrictions, it may fail silently, this is where the app.manfest file comes in.
Although this can also be achieved without it by running the created exe as administrator

# Typed in your cmd
command for creating exe: pyinstaller --onefile --windowed "your_script.py"
exe with app.manifest: pyinstaller --noconsole --onefile --windowed --manifest app.manifest "your_script.py"
