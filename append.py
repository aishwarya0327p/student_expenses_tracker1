n=input("enter the elements:")
l1=[]
while True:
    print("1.append","2.remove","3.update","4.display","5.exit")
    ch=input("enter your choice:")
    if ch=="1":
        l1.append(input("element:"))
        print("element added")
    elif ch=="2":
            l1.remove(input("enter element:"))
    elif ch=="3":
        i=input("enter index:")
        l1=input("new element")
    elif ch=="4":
            print(l1)
    elif ch==5:
        break                        