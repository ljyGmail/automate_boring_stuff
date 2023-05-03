import time
import subprocess

# calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')

notepadProc = subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
print(f'notepadProc.poll() == None: {notepadProc.poll() == None}')

notepadProc.wait()

print(f'notepadProc.poll(): {notepadProc.poll()}')

# Passing Command Line Arguments to the Popen() Function
subprocess.Popen(['C:\\Windows\\notepad.exe', 'data/ch09/bacon.txt'])

# Task Scheduler, launchd, and cron

# Open Websites with Python

# Running Other Python Scripts
subprocess.Popen(
    ['C:\\Python311\\python.exe', 'ch17_time_scheduling_launching/01_time_module.py'])

# Opening Files with Defalut Applications
fileObj = open('data/ch17/hello.txt', 'w')
fileObj.write('Hello, world!')

fileObj.close()

subprocess.Popen(['start', 'data/ch17/hello.txt'], shell=True)

time.sleep(3)
