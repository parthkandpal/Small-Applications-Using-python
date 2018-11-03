'''
@author : Parth Kandpal

There are six steps in the original technique:
Decide on the task to be done.
Set the pomodoro timer (traditionally to 25 minutes).[1]
Work on the task.
End work when the timer rings and put a checkmark on a piece of paper.[5]
If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2.
After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1.
'''

import time
import winsound


def setTimer(checkmark):

    if checkmark <=4:
        countdown=300       #sleeping for 5 minutes
        checkmark += 1
        print("Take a break for 5 minutes")
        for i in range(countdown):
            time.sleep(countdown)
        print("Timer Finished! start your Task again")

        winsound.PlaySound("C:/Windows/media/Alarm01.wav", winsound.SND_ASYNC)

        starttask(Task,checkmark)


    elif checkmark > 4:
        checkmark=0
        print("It's Been more than 4 Checkmarks\n.Its time for a break\nTake a break for 15 minutes")


        time.sleep(900)      #break for 15 minutes 900 seconds

        winsound.PlaySound("C:/Windows/media/Alarm01.wav", winsound.SND_ASYNC)

        print("You have to start you task again")
        starttask(Task)




def starttask(Task,checkmark=0):
    print("Start your Task {}\n".format(Task))
    print("You'll hear an alarm after 25 minutes to take a break")


    print("Sleeping for 25 minutes")
    time.sleep(15000)            #Sleeping for 25 minutes 15000 seconds

    print("25 minutes completed, calling setTimer for taking 5 minute break")
    print("checkmark",checkmark)
    setTimer(checkmark)

# Main method starts here

if __name__=='__main__':
    Task=input("Input task name you want to start\n")
    time.sleep(1)
    print("Enter Ctrl+C after finishing the task\n")

    startime = time.time()

    try:
        starttask(Task,checkmark=0)

    except(KeyboardInterrupt) as e:
        print("Well Done! You completed Task {}! , Now you can enjoy\n".format(Task))

    endtime=time.time()
    totaltime=str((endtime-startime)/60)

    print("You Took {} minutes to complete the task".format(totaltime))

