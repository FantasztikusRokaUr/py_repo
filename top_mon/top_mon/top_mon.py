'''
Created on Aug 6, 2019

@author: Adrian Potoczki
@mail: adrian.potoczki@gmail.com
'''
#!/usr/bin/env python3
import subprocess
import datetime

'''
Here we append the topdata.txt file.
First we open the file, when it's opened, we set it as output file for the subprocess.call shell command.
The data we write in the file:

The TOP 5 CPU using processes (every data returned by the top command) and the current date and time.
'''

with open("/home/mrfox/logging/topdata.txt", "a") as logfile:
    logfile.writelines("\n\nDate and time: " + str(datetime.datetime.now()))
    subprocess.call("top -b -n 1 | head -n 12  | tail -n 5", shell=True, stdout=logfile)
    logfile.writelines("\n\n####################################################################################\n\n\n")

'''
Here we read the text file and get the last lines, where the latest data is.
We get the CPU and Memory usage values by converting lines to strings, then splitting them 
'''

with open("/home/mrfox/logging/topdata.txt", "r") as logfile:
    line = logfile.readlines()    
    no1, no2, no3, no4, no5 = str(line[-12]), str(line[-11]), str(line[-10]), str(line[-9]), str(line[-8])
    process1, process2, process3, process4, process5 = no1.split(), no2.split(), no3.split(), no4.split(), no5.split()
    

    '''
    The 9th and 10th data are the CPU usage and MEM usage in percentage. They are currently strings.
    To add them together we have to convert them to float variables. If the result is returned with "," instead of "."
    for example with CentOS -> it is converted to a float format first with the replace command.
    '''
    
    total_cpu = float(process1[8].replace(",", ".")) + float(process2[8].replace(",", ".")) + float(process3[8].replace(",", ".")) + float(process4[8].replace(",", ".")) + float(process5[8].replace(",", "."))
    total_mem = float(process1[9].replace(",", ".")) + float(process2[9].replace(",", ".")) + float(process3[9].replace(",", ".")) + float(process4[9].replace(",", ".")) + float(process5[9].replace(",", "."))

    '''
    If we find any outstanding values, we write them in a different file, to keep track of the extraordinary events.
    I chose 60% CPU usage and 50% Memory usage as triggering points for logging them as outstanding values.
    In case you want different values, simply change them below in the if statement.
    '''

    if(total_cpu > 60 or total_mem > 50):
        with open("/home/mrfox/logging/outstanding.txt", "a") as outstanding:
            outstanding.writelines("\n\n####################################################################################\
            \n\n\nDate and Time: " + str(datetime.datetime.now()) + "\nTotal CPU Usage:" + str(total_cpu) + "\nTotal MEM Usage:" + \
            str(total_mem) + "\n\n" + no1 + no2 + no3 + no4 + no5)
        