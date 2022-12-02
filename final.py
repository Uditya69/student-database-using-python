from tabulate import tabulate


data = [
        ["uditya",'9434245545'],["utkarsh sharma",'9876961644'],["teja",'6281133492'],
        ["saurav",'6201799836'],["divyanshu",'9696425481'],["haziq",'9797288785'],["shiva",'6396832698']

]
head=["Name","Number"]
def display():
    
    print(tabulate(data,headers=head, tablefmt="grid"))
    conf = input("want to run again (y/n): ")
    if conf == 'y':
        start()
    elif conf == "n":
        print("Goodbye!")
    else:
         print("invalid input")


def start():
    cmd = int(input( """
         ------------------------------------------------------
        |======================================================| 
        |======== Welcome To Student Management System ========|
        |======================================================|
         ------------------------------------------------------

        To View Students Name & Number: enter 1
        To Search Students Name & Number: enter 2
        """ ))
    if cmd == 1:
        display()
    elif cmd == 2:
        i=input("enter name/number to be searched: ")
        res=any(i in sublist for sublist in data)
        ans=(str(res))
        if ans=="True":
                print("Present!")
        else:
            print("Not there!")
        conf = input("want to run again (y/n): ")
        if conf == 'y':
            start()
        elif conf=='n':
            print("Goodbye!")
        else:
            print("invalid input")
    else:
        print("Please select a valid option!")
        conf = input("want to run again (y/n): ")
        if conf == 'y':
            start()
        elif conf=='n':
            print("Goodbye!")
        else:
            print("invalid input")
start()