print("begin game")

num = 10

guessed = False
while not guessed:
    userguess = int(input("Guess a number: "))
    print(userguess)


    if num == userguess:
        print("correct")
        guessed = True
    else:
        print("incorrect")

print("End")

