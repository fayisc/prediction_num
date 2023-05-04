import random

while True:
    play=input("play again? y/n : ")
    if play!="y":
        print("ok bye")
        break

    def myfun():
        a=input("what will be the number ? \n")
        print("your prediction is ",a)
        b=random.randint(0,100)

        if b==a:
            print("your prediction is correct")
            quit
        else :
            print("your prediction is wrong.\n",b,"was the number")

    myfun()
        
