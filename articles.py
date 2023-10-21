# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 22:15:47 2022

@author: sonadisha
"""
import csv

def article_showcase():
    vmenu1=open("articles.csv",'r')
    data=csv.reader(vmenu1)
    records=[]
    lkind=[]
    for i in data:
        records.append(i)
    records.pop(0)
    for p in records:
        if len(p)==0:
            records.remove(p)
    for q in records:
        if q[3] not in lkind:
            lkind.append(q[3])
    
    dart={}
    for m in lkind:
        lart=[]
        for n in records:
            if m==n[3]:
                lart.append(n[:3])
        dart.update({m:lart})
      
    print('''Decoration (D)
Furniture (F)
Gift (G)
Specific (S)''')
    print()
    for s,t in dart.items():
        print(s,":")
        for item in t:
            print(item)
        print()
    vmenu1.close()
    

def article_amount():
    vmenu2=open("articles.csv",'r')    
    data=csv.reader(vmenu2)
    records=[]
    for i in data:
        records.append(i)
    records.pop(0)
    for j in records:
        if len(j)==0:
            records.remove(j)
    
    list_bill=[]
    total=0
    while 1:
        inum=int(input("Enter article number: "))
        iqty=int(input("Enter the quantity required: "))
        for p in records:
            if int(p[0])==inum:
                cost=iqty*int(p[2])
                total=total+cost
                bill=p[1]+'--'+str(iqty)+'--'+str(cost)
                list_bill.append(bill)
        ask2=input("more articles?(y/n)")
        if ask2=='n':
            break
    print()
    print("Your Bill:")
    print("<Article-Quantity-Cost>")
    for q in list_bill:
        print(q)
    print()
    print("Total Cost is:",total)
    vmenu2.close()


def article_add():
    vmenu3=open("articles.csv",'a')
    while 1:
        num=int(input("Article number:"))
        name=input("Article name:")
        price=int(input("Price:"))
        print()
        print('''Decoration (D),
Furniture (F),
Gift (G)
Specific (S)''')
        kind=input("Enter type of article:")
        artlist=[num,name,price,kind]
        x=csv.writer(vmenu3)
        x.writerow(artlist)
        ask2=input("add another?(y/n)")
        if ask2=='n':
            break
    vmenu3.close()


def article_create():
    vmenu4=open("articles.csv",'w')
    head=['Number','Name','Price','Type']
    y=csv.writer(vmenu4)
    y.writerow(head)
    while 1:
        num=int(input("Article number:"))
        name=input("Article name:")
        price=int(input("Price:"))
        print()
        print('''Decoration (D),
Furniture (F),
Gift (G)
Specific (S)''')
        kind=input("Enter type of article:")
        artlist=[num,name,price,kind]
        x=csv.writer(vmenu4)
        x.writerow(artlist)
        ask2=input("add another?(y/n)")
        if ask2=='n':
            break
    vmenu4.close()


while True:
    print("\n\n")
    print("="*50)
    print("\t\t\t\t\tArticles")
    print("-"*50)
    print("(a) Showcase list of articles type-wise")
    print("(b) Find the total amount for required articles")
    print("(c) Add another article")
    print("(d) Create a completely new list of articles")
    print("(e) Leave Topic: Articles")
    ask1=input("Enter your choice:")
    if ask1=="a":
        article_showcase()
    elif ask1=="b":
        article_amount()
    elif ask1=="c":
        article_add()
    elif ask1=="d":
        article_create()
    elif ask1=="e":
        break










