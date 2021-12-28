from numpy import random
print("WELCOME TO VIRTUAL LOVE CALCULATOR : ")
def lovePercentage():
    your_name = input("Enter your name : ")
    crush_name = input("Enter your crush name : ")
    num = random.randint(1, 11, 1)
    love_per  = num[-1]
    print(type(love_per))
    print("Your love percentage is : ", love_per*10)
    greet(love_per)

def greet(value):
    # if value >=80 & value<=100:
    #     print("Your love in boundless : ")
    # elif value>=60 & value<80 :
    #     print("Better understanding : ")
    # elif value>=40 & value<60 : 
    #     print("Rising Love Bird : ")
    # elif value>=20 & value<40 :
    #     print("Number excjanged : ")
    # else:
    #     print("You are not made for these things : ")
    choice()

def choice():
    print("Choose : 1.Continue : 2.Exit : ")
    n = int(input("Your choice : "))
    if(n==1):
        lovePercentage()
    else:
        print("Exited successfully : ")
lovePercentage()

# if love_per>=70 and love_per<100:
#     print("Your understanding & love is boundless : ")
# elif love_per>=40 & love_per<70 :
#     print("Increase your understanding : ")
# elif love_per>=20 & love_per<40 :
#     print("Number exchanged :\nGrowing love bird :  ")
# else:
#     print("Why are you wasting your time : ")