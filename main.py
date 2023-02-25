import add
import Subtract
import multiplication
import Division

def inlt():
    return(list(map(int,input("Enter two numbers : ").split())))


if __name__ == "__main__" :

    print("******************* MENU *******************")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    print("********************************************")

    choice = int(input("Enter choice : (1-4) "))

    if(choice < 1 or choice > 4) :
        print("Invalid choice ! Aborting . . .")
        exit(0);

    inp = inlt()

    if(choice == 1) :
        print(add.add(inp[0], inp[1]))
    elif(choice == 2) :
        print(Subtract.subtract(inp[0], inp[1]))
    elif(choice == 3) :
        print(multiplication.multi(inp[0], inp[1]))
    elif(choice == 4) :
        print(Division.divide(inp[0], inp[1]))
