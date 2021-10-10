# print("This is a health management system which works for 3 person's.\n1: ")
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# def see(a):
#     if a=='1':
#         h=input("For food enter f and for exercise enter e: ")
#         if h=="f":
#             with open("harry-food.txt") as f:
#                 content = f.read()
#                 print(content)
#         elif h=="e":
#             with open("harry-exercise.txt") as f:
#                 content = f.read()
#                 print(content)
#         else:
#             print("Enter f or e !")
#     elif a=='2':
#         r = input("For food enter f and for exercise enter e: ")
#         if r == "f":
#             with open("rohan-food.txt") as f:
#                 content = f.read()
#                 print(content)
#         elif r == "e":
#             with open("rohan-exercise.txt") as f:
#                 content = f.read()
#                 print(content)
#         else:
#             print("Enter f or e !")
#     elif a=='3':
#         H = input("For food enter f and for exercise enter e: ")
#         if H == "f":
#             with open("hammad-food.txt") as f:
#                 content = f.read()
#                 print(content)
#         elif H == "e":
#             with open("hammad-exercise.txt") as f:
#                 content = f.read()
#                 print(content)
#         else:
#             print("Enter f or e !")
#     else:
#         print("Invalid input !!! Enter 1 for  Harry 2 for Rohan 3 for Hammad ")
# def write(b):
#     if b=='1':
#         h = input("For food enter f and for exercise enter e: ")
#         if h=="f":
#             datahF=input("Enter data here\n")
#             with open("harry-food.txt","a") as f:
#                 f.write(str([str(getdate())])+": "+datahF+"\n")
#                 print("[",getdate(),"]",datahF)
#                 print("Successfully writen !!!")
#         elif h=="e":
#             datahE = input("Enter data here\n")
#             with open("harry-exercise.txt","a") as f:
#                 f.write(str([str(getdate())]) + ": " + datahE + "\n")
#                 print("[", getdate(), "]", datahE)
#                 print("Successfully writen !!!")
#         else:
#             print("Invalid input !!!")
#     elif b=='2':
#         r = input("For food enter f and for exercise enter e: ")
#         if r == "f":
#             datarF = input("Enter data here\n")
#             with open("rohan-food.txt", "a") as f:
#                 f.write(str([str(getdate())]) + ": " + datarF + "\n")
#                 print("[", getdate(), "]", datarF)
#                 print("Successfully writen !!!")
#         elif r == "e":
#             datarE = input("Enter data here\n")
#             with open("rohan-exercise.txt","a") as f:
#                 f.write(str([str(getdate())]) + ": " + datarE + "\n")
#                 print("[", getdate(), "]", datarE)
#                 print("Successfully writen !!!")
#         else:
#             print("Enter f or e !")
#     elif b=='3':
#         H = input("For food enter f and for exercise enter e: ")
#         if H == "f":
#             dataHF = input("Enter data here\n")
#             with open("hammad-food.txt","a") as f:
#                 f.write(str([str(getdate())]) + ": " + dataHF + "\n")
#                 print("[", getdate(), "]", dataHF)
#                 print("Successfully writen !!!")
#         elif H=="e":
#             dataHE = input("Enter data here\n")
#             with open("hammad-exercise.txt","a") as f:
#                 f.write(str([str(getdate())]) + ": " + dataHE + "\n")
#                 print("[", getdate(), "]", dataHE)
#                 print("Successfully writen !!!")
#         else:
#             print("Enter f or e !")
#     else:
#         print("Invalid input !!! Enter 1 for  Harry 2 for Rohan 3 for Hammad ")
#
# print("Health Management system:")
# try:
#     while (True):
#         opinion = input("For log enter 1 and to watch enter 2: ")
#         if opinion == '1':
#             print("Choose your name.\n1: Harry\n2: Rohan\n3: Hammad")
#             b = input("Enter the number of person which you want to choose: ")
#             write(b)
#         elif opinion == '2':
#             print("Choose your name.\n1: Harry\n2: Rohan\n3: Hammad")
#             a = input("Enter the number of person which you want to choose: ")
#             see(a)
#         else:
#             print("Invalid input !!!")
#         again = input("To Re-Run this enter 1 and to exit enter 2: ")
#         if again == '1':
#             continue
#         elif again == '2':
#             break
# except Exception as e:
#     print(e)
def getdate():
    import datetime
    return datetime.datetime.now()
def see(a):
    if a=='1':
        h=input("For food enter f and for exercise enter e: ")
        if h=="f":
            with open("harry-food.txt") as f:
                content = f.read()
                print(content)
        elif h=="e":
            with open("harry-exercise.txt") as f:
                content = f.read()
                print(content)
        else:
            print("Enter f or e !")
    elif a=='2':
        r = input("For food enter f and for exercise enter e: ")
        if r == "f":
            with open("rohan-food.txt") as f:
                content = f.read()
                print(content)
        elif r == "e":
            with open("rohan-exercise.txt") as f:
                content = f.read()
                print(content)
        else:
            print("Enter f or e !")
    elif a=='3':
        H = input("For food enter f and for exercise enter e: ")
        if H == "f":
            with open("hammad-food.txt") as f:
                content = f.read()
                print(content)
        elif H == "e":
            with open("hammad-exercise.txt") as f:
                content = f.read()
                print(content)
        else:
            print("Enter f or e !")
    else:
        print("Invalid input !!! Enter 1 for  Harry 2 for Rohan 3 for Hammad ")
def write(b):
    if b=='1':
        h = input("For food enter f and for exercise enter e: ")
        if h=="f":
            datahF=input("Enter data here\n")
            with open("harry-food.txt","a") as f:
                f.write(str([str(getdate())])+": "+datahF+"\n")
                print("[",getdate(),"]",datahF)
                print("Successfully writen !!!")
        elif h=="e":
            datahE = input("Enter data here\n")
            with open("harry-exercise.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + datahE + "\n")
                print("[", getdate(), "]", datahE)
                print("Successfully writen !!!")
        else:
            print("Invalid input !!!")
    elif b=='2':
        r = input("For food enter f and for exercise enter e: ")
        if r == "f":
            datarF = input("Enter data here\n")
            with open("rohan-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + datarF + "\n")
                print("[", getdate(), "]", datarF)
                print("Successfully writen !!!")
        elif r == "e":
            datarE = input("Enter data here\n")
            with open("rohan-exercise.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + datarE + "\n")
                print("[", getdate(), "]", datarE)
                print("Successfully writen !!!")
        else:
            print("Enter f or e !")
    elif b=='3':
        H = input("For food enter f and for exercise enter e: ")
        if H == "f":
            dataHF = input("Enter data here\n")
            with open("hammad-food.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + dataHF + "\n")
                print("[", getdate(), "]", dataHF)
                print("Successfully writen !!!")
        elif H=="e":
            dataHE = input("Enter data here\n")
            with open("hammad-exercise.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + dataHE + "\n")
                print("[", getdate(), "]", dataHE)
                print("Successfully writen !!!")
        else:
            print("Enter f or e !")
    else:
        print("Invalid input !!! Enter 1 for  Harry 2 for Rohan 3 for Hammad ")

print("Health Management system:")
try:
    while (True):
        opinion = input("For log enter 1 and to watch enter 2: ")
        if opinion == '1':
            print("Choose your name.\n1: Harry\n2: Rohan\n3: Hammad")
            b = input("Enter the number of person which you want to choose: ")
            write(b)
        elif opinion == '2':
            print("Choose your name.\n1: Harry\n2: Rohan\n3: Hammad")
            a = input("Enter the number of person which you want to choose: ")
            see(a)
        else:
            print("Invalid input !!!")
        again = input("To Re-Run this enter 1 and to exit enter 2: ")
        if again == '1':
            continue
        elif again == '2':
            break
except Exception as e:
    print(e)