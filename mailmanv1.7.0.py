#!/usr/bin/env python3

##################################
# Program Name: MAILMAN          #
# Version: 1.7.0                 #
# Author: Ethan Hicks            #
# Published: 9/18/2015           #
################################## 

import os
import tkinter
import smtplib
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL
from email.mime.text import MIMEText

#Get the current/target directory
path = os.getcwd()
list_of_files = list(os.walk(path))
#print(path)
extensions = []
#open the reporting file
window = tkinter.Tk()
window.wm_title('MAILMANv1.7.0')
label = tkinter.Label(window, text = 'Welcome to Mailman!')
label.pack()
frame1 = tkinter.Frame(window)
frame1.pack()
frame2 = tkinter.Frame(window)
frame2.pack()

button00 = tkinter.Button(window, text = 'Execute', fg = 'red', font = ('courier',12),
                          command = lambda: Execute('os'))
button00.pack()

def Execute(a):

    if a == 'os':
        with open("systemstats.txt","w") as sysstats:
            sysstats.write(path )
            #Get the filenames in the target director
            for files in list_of_files:
                for filename in files[-1]:
                    sysstats.write('{}{}'.format(filename,"    "))
                    #print(filename)
                    line = filename[::-1].lower().split('.')[0][::-1]
                    #summarize and count
                    for row in extensions:
                        if line in row[0]:
                            row[1] +=1
                            break
                    else:
                        extensions.append([line,1])
            for line in sorted(extensions):
                #print('{}: {}'.format(line[0],line[1]))
                sysstats.write('{}: {}'.format(line[0],line[1]))
                #sysstats.close()

        with open('systemstats.txt','r') as fp:
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
