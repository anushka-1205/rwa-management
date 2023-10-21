# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 18:11:01 2022

@author: sonadisha
"""
import pickle

def food_create():
    fmenu1=open("food.dat",'wb')
    while True:
        topic=input("Choose course: Snacks/Main_course/Dessert/Beverage/Extras: ")
        list_topic=[]
        while 1:
            name=input("Enter name of food item: ")
            price=int(input("Enter price of one piece: "))
            qty=int(input("Enter quantity of the item needed: "))
            list_item=[name,price,qty]
            list_topic.append(list_item)
            ask2=input("add another?(y/n)")
            if ask2=='n':
                dict_topic={topic:list_topic}
                pickle.dump(dict_topic,fmenu1)
                break
        ask3=input("add another course?(y/n)")
        if ask3=='n':
            break
    fmenu1.close()
    
def food_showcase():
    fmenu2=open("food.dat",'rb')
    tlist=[]
    try:
        while True:
            x=pickle.load(fmenu2)
            tlist.append(x)
    except:
        print("(search complete)")
    print()
    print("<item,price,quantity>")
    for i in tlist:
        print()
        for s,t in i.items():
            print(s)
            for j in t:
                print(j)
    fmenu2.close()

def food_search():
    fmenu3=open("food.dat",'rb')
    tlist=[]
    item=input("Enter the name of the item to be searched:")
    try:
        while True:
            y=pickle.load(fmenu3)
            tlist.append(y)
    except:
        print("(search complete)")
    its='no'
    for k in tlist:
        for m,n in k.items():
            for l in n:
                if l[0]==item:
                    print("In",m,":",l[0],", price-",l[1],", quantity-",l[2])
                    its='yes'
    if its=="no":
        print("The item is not present in the menu.")
    fmenu3.close()


while True:
    print("\n\n")
    print("="*46)
    print("\t\t\t\t\tFOOD")
    print("-"*46)
    print("(a) Showcase current Menu")
    print("(b) Search for an item from the current Menu")
    print("(c) Create a new Menu")
    print("(d) Leave Topic: Food")
    ask1=input("Enter your choice:")
    if ask1=="a":
        food_showcase()
    elif ask1=="b":
        food_search()
    elif ask1=="c":
        food_create()
    elif ask1=="d":
        break





















