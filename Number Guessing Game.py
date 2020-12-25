import random
a=random.randrange(1,101)
print("\n................................WELCOME TO NUMBER GUESSING GAME........................................\n")
print("\nInstructions\n1.You guess a number\n2.You have to guess a number between 1 to 100\n3.You will get 20 chances and if you fail in subsequent tries you will get a hint\n4.First you have to enter the number of times you took to guess the number correctly in previous attemt.If it is your 1st attemp sset it as zero.")
c=int(input("Enter the no. of previous tries to complete:- "))
print("\n Best of Luck")
for i in range(21):
    b=int(input("Enter Your Guess"))
    if(b==a):
        print("You Won!!!! and the number of tries it took is",i+1)
        d=i+1
        if(d>c):
            print("But you have completed the task in greater no. of attempts so try again!")
        elif(d<c):
            print("Wow! it took least time to guess this time!Congratulations")

    elif(b<a):
        print("Enter a greater number.")
    elif(b>a):
        print("Enter a lesser number.")
print("The correct number is:- ",a)
print("\n............................GAME OVER................................................")
