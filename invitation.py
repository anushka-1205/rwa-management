# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:39:17 2022

@author: sonadisha
"""
import csv

def invit_draft():
    imenu1=open("draft.txt",'r')
    formats=imenu1.readlines()
    print('--'*26)
    for i in formats:
        print(i)
    print('--'*26)
    imenu1.close()
        

def invit_showcase():
    print('''RWA Member (RM)
Guest (G)
Participant (P)
Special Guest (SG)''')
    imenu2=open("invitations.csv",'r')
    info1=csv.reader(imenu2)
    info2=[]
    for i in info1:
        if len(i)>0:
            info2.append(i)
    info2.pop(0)
    for j in info2:
        print(j)
    imenu2.close()
    

def invit_add():
    imenu3=open("invitations.csv",'a')
    t=input("Enter category(P/G/RM/SG): ")
    n=input("Enter name: ")
    cont=input("Enter contact number: ")
    ad=input("Enter address: ")
    email=input("Enter email id: ")
    rec=[t,n,cont,ad,email]
    x=csv.writer(imenu3)
    x.writerow(rec)
    imenu3.close()


def invit_emailid():
    print('''RWA Member (RM)
Guest (G)
Participant (P)
Special Guest (SG)''')
    imenu4=open("invitations.csv",'r')
    info3=csv.reader(imenu4)
    info4=[]
    for i in info3:
        if len(i)>0:
            info4.append(i)
    info4.pop(0)
    cat=[]
    for j in info4:
        if j[0] not in cat:
            cat.append(j[0])
    ilist1=[]
    for k in info4:
        email=k[4].split('@')
        name=email[0]
        ilist1.append([k[0],name])
    idict1={}
    for p in cat:
        ilist2=[]
        for q in ilist1:
            if q[0]==p:
                ilist2.append(q[1])
        idict1.update({p:ilist2})
    ask2=input("Enter the category of people you want ids of: ")
    its='no'
    for s,t in idict1.items():
        if s==ask2:
            print(t)
            its='yes'
    if its=='no':
        print("No one from this category found")
    imenu4.close()


while True:
    print("\n\n")
    print("="*55)
    print("\t\t\t\t\tInvitations")
    print("-"*55)
    print("(a) Display Draft for invitation")
    print("(b) Display information about people in the event")
    print("(c) Add information about another member")
    print("(d) Get email ids of all the people from a category")
    print("(e) Leave Topic: Invitations")
    ask1=input("Enter your choice:")
    if ask1=="a":
        invit_draft()
    elif ask1=="b":
        invit_showcase()
    elif ask1=="c":
        invit_add()
    elif ask1=="d":
        invit_emailid()
    elif ask1=="e":
        break














