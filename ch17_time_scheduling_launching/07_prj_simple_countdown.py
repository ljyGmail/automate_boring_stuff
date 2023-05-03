import time
import subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file
subprocess.Popen(['start', 'data/ch17/alarm.wav'], shell=True)
