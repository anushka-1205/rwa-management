
while True:
    print("\n\n\n")
    print("=="*25)
    print("\t\t\tWelcome to RWA System")
    print("=="*25)
    print("A. The RWA Group")
    print("B. Loan and Bill Department")
    print("C. Society Grocery")
    print("D. Privileges to the Orphanage/ Old Age Home")
    print("E. Events in the Society")
    print("F. EXIT")
    ask=input("Enter your choice(A-F): ")
    if ask=="A":
        while 1:
            print("--"*20)
            print("\t\t\tThe RWA Group")
            print("--"*20)
            print("1. Members")
            print("2. Notice Board")
            print("3. File a complaint")
            print("4. Leave The RWA Group")
            choice=input("Enter your pick: ")
            if choice=="1":
                pass
                #import govbody
            elif choice=="2":
                pass
                #import noticeboard
            elif choice=="3":
                pass
                #import complain
            elif choice=="4":
                break
    elif ask=="B":
        pass
        #import loan_bill
    elif ask=="C":
        pass
        #import grocery
    elif ask=="D":
        while 1:
            print("--"*30)
            print("\t\tPrivileges to the Orphanage/ Old Age Home")
            print("--"*30)
            print("1. Orphanage")
            print("2. Old Age Home")
            print("3. Leave Privileges to the Orphanage/ Old Age Home")
            choice=input("Enter your pick: ")
            if choice=="1":
                pass
                #import orphanage
            elif choice=="2":
                pass
                #import old_age_home
            elif choice=="3":
                break
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
        print("THANK YOU!!")
        break
    





