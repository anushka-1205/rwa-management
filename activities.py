# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:01:40 2022

@author: sonadisha
"""
import pickle

def activ_create():
    amenu1=open("activities.dat",'wb')
    actdict1={}
    while 1:
        kind=input("Enter type of activity(Games/Dance/Sing/Play): ")
        num=int(input("Number of activities to add in this category: "))
        actlist1=[]
        for i in range(num):
            nu=input("Enter id number:")
            n=input("Enter name: ")
            t=int(input("Enter time duration(min): "))
            actlist1.append([nu,n,t])
        actdict1.update({kind:actlist1})
        pickle.dump(actdict1,amenu1)
        ask2=input("Add for another type?(y/n) ")
        if ask2=='n':
            break
    amenu1.close()

def activ_showcase():
    amenu2=open("activities.dat",'rb')
    try:
        while True:
            x=pickle.load(amenu2)
    except:
        print("(search complete)")
    print("Activities in respective categories with time duration(min):\n")
    for s,t in x.items():
        print(s)
        for k in t:
            print(k)
        print()
    amenu2.close()

def activ_time():
    actlist2=[]
    while 1:
        per=input("Enter id number of the activity required: ")
        actlist2.append(per)
        ask3=input("add another?(y/n) ")
        if ask3=='n':
            break
    amenu3=open("activities.dat",'rb')
    try:
        while True:
            x=pickle.load(amenu3)
    except:
        print("(search complete)\n")
    t_time=0
    actlist3=[]
    for s,t in x.items():
        for k in t:
            if k[0] in actlist2:
                actlist3.append(k)
                t_time=t_time+k[2]
    print("Total time duration:",t_time)
    print(actlist3)
    r_time=int(input("Enter required time for the event(min): "))
    
    if r_time>=t_time:
        print("Your total event time fit well with the time duration of the activities.")
    else:
        diff=t_time-r_time
        print("Time duration exceeds the total event time by",diff,"minutes")
        ask4=input("Do you want to remove some activity from your list?(y/n)")
        if ask4=='y':
            while t_time>r_time:
                rem=eval(input("Enter in list the id numbers of the activities to remove: "))
                for p in actlist3:
                    if p[0] in rem:
                        actlist3.remove(p)
                        t_time=t_time-p[2]
                print("Current Time Duration",t_time)
            print("\nTotal time duration:",t_time)
            print(actlist3)
            print("Now, your total event time fit well with the time duration of the activities.")
    amenu3.close()
  

while True:
    print("\n\n")
    print("="*58)
    print("\t\t\t\t\t\tActivities")
    print("-"*58)
    print("(a) Create a participant list")
    print("(b) Display participant list")
    print("(c) Total time calculated with the required participants")
    print("(d) Leave Topic: Activities")
    ask1=input("Enter your choice:")
    if ask1=="a":
        activ_create()
    elif ask1=="b":
        activ_showcase()
    elif ask1=="c":
        activ_time()
    elif ask1=="d":
        break

















