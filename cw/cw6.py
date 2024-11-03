
try:
    print("start code")
    print(10/0)
    print("endcode")
except:
    print("code after error")


try:
    print("start code")
    print("2" + 2)
    print(number)
    print(10/0)
    print("end code")


except ZeroDivisionError:
    print("zero error")
    
