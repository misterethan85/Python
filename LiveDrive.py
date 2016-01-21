import tkinter  
import os
#frome os import subprocess


path = os.getcwd()
list_of_files = list(os.walk(path))
files = []
for i in list_of_files:
    for filename in i[-1]:
        if filename.endswith('.py'):
            files.append(filename)
#print(files)
window = tkinter.Tk()
window.wm_title('LiveDrive')
label = tkinter.Label(window, text = 'Welcome to the Live USB creator utility!\n Choose Your Distribution of choice.')
label.pack()
frame1 = tkinter.Frame(window)
frame1.pack()
frame2 = tkinter.Frame(window)
frame2.pack()
i = 0
bttn = []
for r in range(len(files)):
    for c in range(1):
        bttn.append(tkinter.Checkbutton(frame1, text = files[i], fg = 'blue', font = ('courier',11),
                    command = lambda: Execute('idk')))
        bttn[i].pack()#grid(row = r, column = c)
        i += 1

label1 = tkinter.Label(frame2, text='Now check which filesystem to write the ISO image to.')
label1.pack()

z = 0
iso = []
#need to figure out usb event detection, append to mount_points list then it will be properly referencing the usb's.
mount_points = '1234'
for r in range(len(mount_points)):
    for c in range(1):
        iso.append(tkinter.Checkbutton(frame2, text = files[z], fg = 'purple', font = ('courier', 11),
                   command = lambda: Execute('idk')))
        iso[z].pack()#grid(row = r,column = c)
        z += 1


button00 = tkinter.Button(window, text = 'Execute', fg = 'red', font = ('courier',12),
                          command = lambda: Execute('os'))
button00.pack()


def Execute(a):

    if a == 'os':
      print("WINNING")

        
    
window.mainloop()

