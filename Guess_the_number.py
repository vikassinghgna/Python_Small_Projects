import random
computer = random.randint(1,100)
guess=0
while True:
    user = int(input("Enter no. between 1 and 100: "))
    if(user<1 or user>100):
        print("Enter no. between 1 and 100 only")
        continue
    guess+=1
    if(computer<user):
        print("Lower number please")
    elif(computer>user):
        print("Higher number please")
    else:
        print("You matcched the value finally at",guess,"Guesses")
        break
    