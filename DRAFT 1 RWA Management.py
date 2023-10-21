# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 01:41:48 2022

@author: sonadisha
"""


while True:
    print("\n\n\n")
    print("=="*20)
    print("\t\tWelcome to RWA System")
    print("=="*20)
    print("A. Members of the RWA Group")
    print("B. Society Bank")
    print("C. Society Grocery")
    print("D. Facilities for the ones in need")
    print("E. Events in the Society")
    print("F. EXIT")
    ask=input("Enter your choice(A-F): ")
    if ask=="A":
        pass
    elif ask=="B":
        import bank
    elif ask=="C":
        import grocery
    elif ask=="D":
        pass
    elif ask=="E":
        while 1:
            print("--"*20)
            print("\t\t\t\tEVENTS")
            print("--"*20)
            print("1. Food")
            print("2. Articles")
            print("3. Activities")
            print("4. Invitations")
            print("5. Leave EVENTS")
            choice=input("Enter your pick: ")
            if choice=="1":
                import food
            elif choice=="2":
                import articles
            elif choice=="3":
                import activities
            elif choice=="4":
                import invitation
            elif choice=="5":
                break
    elif ask=="F":
        break





