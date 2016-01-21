#!/usr/bin/env python3

import tkinter
from tkinter import filedialog
import csv
import smtplib
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL
from email.mime.text import MIMEText

window = tkinter.Tk()
window.wm_title('File Editor')
frame1 = tkinter.Frame(window)
frame1.pack()
frame2 = tkinter.Frame(window)
frame2.pack()
frame3 = tkinter.Frame(window)
frame3.pack()

label1 = tkinter.Label(frame1, text='Input File:',fg='blue')
label1.grid(row=1,column=1)

entry1 = tkinter.Entry(frame1)
entry1.grid(row=1,column=2)

browse1 = tkinter.Button(frame1, text='Browse',
                         command = lambda: Input_Browse_File('a'))
browse1.grid(row=1,column=3)

label2 = tkinter.Label(frame2, text='Output File:',fg='blue')
label2.grid(row=2,column=1)

entry2 = tkinter.Entry(frame2)
entry2.grid(row=2,column=2)

browse2 = tkinter.Button(frame2, text='Browse',
                         command = lambda: Output_Browse_File('o'))
browse2.grid(row=2,column=3)

process_button = tkinter.Button(frame2, text = 'Process File',fg='blue',
                                command = lambda: Process_File('p'))
process_button.grid(row=3,column=1)

mail_button = tkinter.Button(frame2, text = 'Mail File',fg='red',
                                command = lambda: Process_File('m'))
mail_button.grid(row=3,column=3)


x = ''
y = ''
op = ''
m = ''

def Input_Browse_File(a):
    if a == 'a':    
        window.filename = filedialog.askopenfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
        text = window.filename.split('/')
        filename = text[-1]
        entry1.insert(0,filename)
        #print(filename)
def Output_Browse_File(o):
    if o == 'o':
        window.filename = filedialog.asksaveasfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
        text = window.filename.split('/')
        filename = text[-1]
        entry2.insert(0,filename)
        #print(filename)
        
def Process_File(p):
    global x,y,op
    if p == 'p':
        y = entry1.get()
        with open(y,'r') as newfile:
            var = newfile.readlines()
            source = []
            for i in var:
                i = i.strip()
                source.append(i)
            #print(source)
            for i in range(len(source)):
                mini = min(source[i:])
                min_index = source[i:].index(mini)
                source[i + min_index] = source[i] 
                source[i] = mini                  

            z = entry2.get()
            with open(z,'w') as summary_file:
                for row in source[1:]:
                    contents = summary_file.write(row+'\n')
                    r = 'Lines Written:{}'.format(len(source))
                print(r)
                
def mail_file(m):
    """ Sends summarized file via SMTP mail engine"""

    if m == 'm':
        z = entry2.get()
        with open(z,'r') as fp:
            data = fp.read()
            login, password = 'misterethan85@gmail.com', getpass('Gmail password:')
            recipients = ['12barajasc@gmail.com']
            # create message
            msg = MIMEText(data)
            msg['Subject'] = Header('System Report', 'utf-8')
            msg['From'] = login
            msg['To'] = '12barajasc@gmail.com'#", ".join(recipients)
            # send it via gmail
            s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
            s.set_debuglevel(1)
            try:
                s.login(login, password)
                s.sendmail(msg['From'], recipients, msg.as_string())

            finally:

                    s.quit()








           
window.mainloop()


