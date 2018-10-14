'''Create a simple timesheet app that records when you type a person’s name and uses the current time to clock them in or out.
'''
import datetime


personInDict={}
personOutDict={}

def Menu():

    print("Press 1 to enter inTime\nPress 2 to enter outTime\t Press 0 to quit")
    label:input
    key=int(input())
    if key==1:
        print("Please enter the name of the person Entering")
        personname=input()
        personIntime=datetime.datetime.now().time()
        personInDict[personname]=str(personIntime)
        print("Person {}, entered at {} recorded successfully".format(personname,personIntime))
        Menu()
    elif key==2:
        print("Please enter the name of the person Leaving")
        personname = input()
        personOuttime = datetime.datetime.now().time()
        print(personOuttime)
        personOutDict[personname] = str(personOuttime)
        print("Person {}, entered at {} recorded successfully".format(personname, personOuttime))
        Menu()
    elif key==0:
        return  0
    else:
        print("Invalid input /t Please input 1 for Intime and 2 for Outtime")
        Menu()
print(str(datetime.datetime.now().time()))
Menu()
print("Total people entered with InTime {}".format(personInDict))
print("Total people left with OutTime {}".format(personOutDict))