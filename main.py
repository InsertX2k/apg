# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.tix import *
from awesometkinter import DEFAULT_COLOR, Button3d
import awesometkinter as atk
from subprocess import getoutput
from sys import getrecursionlimit, setrecursionlimit
import sys
import configparser

# declaring a variable for font size.
font_size = 16


# Defining a class representing the Object Oriented Programming Style of the GUI.
class PasswordGeneratorGUI(Tk):
    """
    A class represents the main Graphical User Interface of the Program "Advanced Password Generator" by Insertx2k Dev (Mr.X)

    To import this or use this manually, Try doing:
    ```py
    from main import *
    from sys import getrecursionlimit, setrecursionlimit

    if __name__ == '__main__':
        setrecursionlimit(1000)
        somevariable = PasswordGeneratorGUI()
        somevariable.mainloop()
    ```

    """
    global font_size

    def __init__(self):
        """
        The method that represents the Tkinter interpreter of the Graphical User Interface of the program "Advanced Password Generator"
        
        Try:
        ```py
        from main import *
        from sys import getrecursionlimit, setrecursionlimit

        if __name__ == '__main__':
            setrecursionlimit(1000)
            x = PasswordGeneratorGUI.__init__()
            x.mainloop()
        ```

        It is exactly the same as:
        
        ```py
        from main import *
        from sys import getrecursionlimit, setrecursionlimit

        if __name__ == '__main__':
            setrecursionlimit(1000)
            x = PasswordGeneratorGUI()
            x.mainloop()
        ```

        But with just `__init__()` function being called in the first example.
        """
        global generatedPassword, font_size
        super().__init__()
        # defining the root properties.
        self.title("Advanced Password Generator")
        self.geometry('600x300')
        self.configure(background=DEFAULT_COLOR)
        self.minsize(600, 300)
        self.maxsize(600, 300)
        self.resizable(False, False)

        # declaring the configparser's processor variable.
        configProcessor = configparser.ConfigParser()
        # Reading the configuration file "config.ini"
        configProcessor.read("config.ini")



        def settingsWindow():
            # defining the settingsRoot window.
            settingsRoot = Tk()
            settingsRoot.geometry('640x480')
            settingsRoot.minsize(640, 480)
            settingsRoot.title("Settings @ Advanced Password Generator")
            settingsRoot.configure(background=DEFAULT_COLOR)
            settingsRoot.resizable(False, False)

            def showAboutWindow():
                # defining the about window.
                aboutwindow = Toplevel()
                aboutwindow.title("About Advanced Password Generator")
                aboutwindow.minsize(640, 480)
                aboutwindow.resizable(True, True)
                aboutwindow.configure(background=DEFAULT_COLOR)

                # attempting to load an icon file for the window.
                try:
                    aboutwindow.iconbitmap("icon.ico")
                except Exception as excpt3:
                    print(f"error: unable to load icon for about & licenses window due to exception:\n{excpt3}")
                    pass

                # defining function for increasing font size
                def incrfontsize(keybinding_arg):
                    global font_size

                    # checking if font size is bigger or equal to 70.
                    if int(font_size) >= 70:
                        messagebox.showerror("Increase font size",
                                             "Is your eyesight really that low?, if yes, then I'm sorry you can't increase the font size more than this.")
                        return False
                    else:
                        font_size += 1

                    showabout.configure(font=("Consolas", font_size))
                    return None

                # defining a tooltip.
                tip = Balloon(aboutwindow)

                # defining function for decreasing font size.
                def decrfontsize(keybinding_arg):
                    """
                    Call the function to decrease the font size of the text shown in "About & Licenses" window.

                    It is always better to bind this function to a something better, like the root of the window.

                    Example:
                    ```py
                    aboutwindow.bind("<Control-d>", decrfontsize)
                    aboutwindow.bind("<Control-D>", decrfontsize)
                    ```
                    """
                    global font_size

                    # checking if font size is equal to 0 or less.
                    if int(font_size) <= 4:
                        messagebox.showerror("Decrease font size",
                                             "Is your screen really that big?, You can't decrease the font size more than this.")
                        return False
                    else:
                        font_size -= 1

                    showabout.configure(font=("Consolas", font_size))
                    return None

                # defining the scrolledtext widget that will show the about and licenses text.
                showabout = scrolledtext.ScrolledText(aboutwindow, cursor='arrow', background=DEFAULT_COLOR,
                                                      selectbackground='orange', highlightbackground='orange',
                                                      font=("Consolas", font_size), foreground='white')
                showabout.pack(expand=1, fill='both')
                # inserting some text into the scrolledtext widget.
                showabout.delete(1.0, END)
                showabout.insert(END, """About 'Advanced Password Generator' by Insertx2k Dev (Mr.X)

'Advanced Password Generator' is a free software, which means you are allowed to modify or redistribute it under the terms of the GNU General Public License v2.0 or later @ Free Software Foundation.

'Advanced Password Generator' is licensed under the GNU General Public License v2.0 or later, however, other components this software use aren't licensed in the same license, that's why there is a licenses section in this about window.

=====================
Let's start with this program's license:

License for 'Advanced Password Generator' by Insertx2k Dev (Mr.X).

'Advanced Password Generator' is licensed under the GNU General Public License v2.0.

License is shown below: 

 A Simple GUI for generating secure passwords for online banking and social media accounts and so on.
 Copyright (C) 2021 - Insertx2k Dev (Mr.X) or The X Software Foundation
 
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

=====================

This program uses the following 3rd party components which may use a different license than this software does:
* Awesometkinter by Mahmoud Elshahat.
* APG Service (Advanced Password Generator Service) by Insertx2k Dev (Mr.X).

=====================

License for APG Service (Advanced Password Generator Service) by Insertx2k Dev (Mr.X).

APG Service is licensed under GNU General Public License v2.0 or later @ Free Software Foundation.

License for APG Service is shown below:

 Necessary coreutils for building distributable binaries of Advanced Password Generator GUI
 Copyright (C) 2021 - Insertx2k Dev (Mr.X) or The X Software Foundation
 
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

=====================



""")

                showabout.configure(state='disabled')

                # binding Control - d and Control - i for decreasing and increasing font size.
                aboutwindow.bind("<Control-d>", decrfontsize)
                aboutwindow.bind("<Control-i>", incrfontsize)
                aboutwindow.bind("<Control-D>", decrfontsize)
                aboutwindow.bind("<Control-I>", incrfontsize)

                tip.bind_widget(showabout, balloonmsg="""Accessibility Options are here!, You can right now increase or decrease the font size depending on your needs.
To decrease the font size you can use the hotkey (Control - D).
To increase the font size you can use the hotkey (Control - I).

Feel free to enjoy using Mr.X's software with your high-quality big screen or low eyesight.

""")

                # making the about window appear to the user.
                aboutwindow.mainloop()

                return None



            def discardChanges():
                """
                This function destroys the settings window and 
                """
                # attempting to destroy the settings window.
                try:
                    settingsRoot.destroy()
                    # aboutwindow.destroy()
                    return True
                except Exception as excpt6:
                    print(f"Unable to destroy the settings Window due to Exception\n{excpt6}")
                    return False
                
                return None



            # trying to set an icon image for the settings window.
            try:
                settingsRoot.iconbitmap("icon.ico")
            except Exception as excpt1:
                print(f"error: could not load icon file for the settings window due to exception\n{excpt1}")
                pass

            lbl = Label(settingsRoot, text="Advanced Password Generator Settings", font=("Arial Bold", 24),
                        foreground='white', background=DEFAULT_COLOR)
            lbl.place(x=10, y=10)

            lbl1 = Label(settingsRoot, text="Settings will be saved in 'config.ini' file.", background=DEFAULT_COLOR,
                         foreground='white')
            lbl1.place(x=10, y=60)

            lbl2 = Label(settingsRoot, text="How many lowercase characters do you want your password to contain?:",
                         font=("Arial", 12), background=DEFAULT_COLOR, foreground='white')
            lbl2.place(x=10, y=85)

            enterlowercase_charsindex = ttk.Entry(settingsRoot, width=100)
            enterlowercase_charsindex.place(x=10, y=110)

            lbl3 = Label(settingsRoot, text="How many uppercase characters do you want your password to contain?:",
                         font=("Arial", 12), background=DEFAULT_COLOR, foreground='white')
            lbl3.place(x=10, y=135)

            enteruppercase_charsindex = ttk.Entry(settingsRoot, width=100)
            enteruppercase_charsindex.place(x=10, y=160)

            lbl4 = Label(settingsRoot, text="How many numbers do you want your password to contain?:",
                         font=("Arial", 12), background=DEFAULT_COLOR, foreground='white')
            lbl4.place(x=10, y=185)

            enternumbers_index = ttk.Entry(settingsRoot, width=100)
            enternumbers_index.place(x=10, y=210)

            lbl5 = Label(settingsRoot, text="How many special Characters do you want your password to contain?:",
                         font=("Arial", 12), background=DEFAULT_COLOR, foreground='white')
            lbl5.place(x=10, y=235)

            enterspecial_charsindex = ttk.Entry(settingsRoot, width=100)
            enterspecial_charsindex.place(x=10, y=260)

            lbl6 = Label(settingsRoot, text="When you are done, don't forget to click on the save button.",
                         font=("Arial", 12), background=DEFAULT_COLOR, foreground='white')
            lbl6.place(x=10, y=310)

            # defining the buttons to save and close the window.

            savebtn = ttk.Button(settingsRoot, text="Save Changes", command=None)
            savebtn.place(x=10, y=350, relwidth=0.450, relheight=0.115)

            closebtn = ttk.Button(settingsRoot, text="Close & Discard all Changes", command=discardChanges)
            closebtn.place(x=330, y=350, relwidth=0.450, relheight=0.115)

            # defining the show about and licenses button.

            showabout_license = ttk.Button(settingsRoot, text="About & Licenses", command=showAboutWindow)
            showabout_license.place(x=180, y=410, relwidth=0.450, relheight=0.115)

            # calling the mainloop of the settingsroot to show the settingsroot window.
            settingsRoot.mainloop()

        # trying to load the icon file icon.ico into the window.
        try:
            self.iconbitmap("icon.ico")
        except Exception as excpt0:
            print(f"error: could not load icon file for window because: {excpt0}")
            pass


        def generateAPassword():
            """
            Generates a password with the given details in `config.ini` file.

            Yes, this function actually reads data from the file `config.ini`.

            Then, it returns the generated password to the user in the ScrolledText area `passshow`.
            """
            # attempting to get configuration data from the config file "config.ini"
            try:
                lengthofNumbers = int(configProcessor['APGServiceCall']['LengthOfNumbers'])
                print(f"[GET]:Got the length of Numbers in generated password: {lengthofNumbers}")
                lengthofSpecialChars = int(configProcessor['APGServiceCall']['LengthOfSpecialChars'])
                print(f"[GET]:Got the length of Special Characters in generated password: {lengthofSpecialChars}")
                lengthofUpperCaseChars = int(configProcessor['APGServiceCall']['LengthOfUpperCaseChars'])
                print(f"[GET]:Got the length of uppercase characters in generated password: {lengthofUpperCaseChars}")
                lengthofLowerCaseChars = int(configProcessor['APGServiceCall']['LengthOfLowerCaseChars'])
                print(f"[GET]:Got the length of lower case characters in generated password: {lengthofLowerCaseChars}")
            except Exception as excpt3: # when an exception occurs.
                messagebox.showerror("Unable to get data from Config file", f"Unable to get data from configuration file due to the error\n{excpt3}\nThe program will terminate itself right now after you press the button OK.")
                sys.exit(12) # Raises the error code 12 meaning the process has failed.
            
            # now let's clear the text area and inform the user of a background process.
            passshow.configure(state='normal')
            # passshow.delete(1.0, END)
            passshow.insert(END, "\n(Initializing Password Generator Service)")
            passshow.configure(state='disabled')
            
            initialize = getoutput("apgservices.exe")
            passshow.configure(state='normal')
            # passshow.delete(1.0, END)
            passshow.insert(END, f"\n{initialize}")
            # passshow.delete(1.0, END)
            passshow.insert(END, "\n(Initialized service!)")
            passshow.configure(state='disabled')
            passshow.configure(state='normal')
            passshow.insert(END, "\n\n(Preparing to generate your password...)")
            passshow.configure(state='disabled')

            password = getoutput(f"apgservices.exe {lengthofNumbers} {lengthofSpecialChars} {lengthofUpperCaseChars} {lengthofLowerCaseChars}")
            passshow.configure(state='normal')
            passshow.delete(1.0, END)
            passshow.insert(END, password)
            passshow.configure(state='disabled')
            

            # print("The user wants to generate a password.")
            return None




        lbl = Label(self, text="Advanced Password Generator", font=("Arial Bold", 24), background=DEFAULT_COLOR,
                    foreground='white')
        lbl.place(x=50, y=15)
        lbl2 = Label(self, text="Your generated password is:", font=("Arial", 12), background=DEFAULT_COLOR,
                     foreground='white')
        lbl2.place(x=30, y=60)

        passshow = scrolledtext.ScrolledText(self, cursor='arrow', highlightbackground='orange',
                                             background=DEFAULT_COLOR, font=("Arial", 14), foreground='white',
                                             selectbackground='orange')
        passshow.place(x=30, y=85, relwidth=0.900, relheight=0.400)
        # clearing scrolledtext area.
        passshow.delete(1.0, END)
        passshow.insert(END, "(NO GENERATED PASSWORD)")
        passshow.configure(state='disabled')

        # defining the go to settings button.
        go_settings_btn = Button3d(self, text="Settings", command=settingsWindow)
        go_settings_btn.place(x=30, y=220, relheight=0.200, relwidth=0.400)

        # defining the go generate button.
        go_generate_btn = Button3d(self, text="Generate", command=generateAPassword)
        go_generate_btn.place(y=220, x=330, relheight=0.200, relwidth=0.400)


# if program was executed as a Python 3.x.x Script file,
if __name__ == '__main__':  # execute the given code in this statement.
    setrecursionlimit(1000)  # set recursion limit to 1000 (1k)
    x = PasswordGeneratorGUI()  # take a clone of the class PasswordGeneratorGUI()
    x.mainloop()  # call it's method "mainloop()"
else:  # otherwise, if the program was executed as a Python module.
    pass  # Don't do anything.
