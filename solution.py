userInput=int(input("Enter a number to see a tree: "))
counter=1
multiply=2

while(counter<=userInput):
    starCounter=1
    while(starCounter<=counter):
        print(multiply, end=" ")
        starCounter=starCounter + 1
        multiply=multiply+2
       
    counter=counter+1
    multipy=counter
    print(" ")
