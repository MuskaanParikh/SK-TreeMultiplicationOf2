userInput=int(input("Enter a number to see a tree: "))
multiply=2

for i in range(1,userInput+1):
    for j in range(i):
        print(multiply, end=" ")
        multiply=multiply+2
    print(" ")
