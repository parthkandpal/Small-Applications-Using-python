import subprocess, time
#subprocess.Popen('C:\\Windows\\System32\\calc.exe')

print("For how much seconds you want to set countdown?")
countdown=int(input())

print("Staring Countdown.........")
time.sleep(1)
print("You ready...")
time.sleep(1)
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print("3")
time.sleep(2)
print("Let's Go")

for i in range(countdown,0,-1):

    time.sleep(1)
    print("Countdown...here {}".format(i))

print("Countdown Finished!")

subprocess.Popen(['start', 'alarm.wav'], shell=True)
