num = int(input("Enter the number: "))
match num:
    case 1:
        print("your choice is 1")
    case 10:
        print("Your choice is 10")
    case 15:
        print("Your choice is 15")
    case _:
        print("Invalid choice!")

#match case statement is used to match the values to num input if the user enters 1, 10, 15 as input the code output's accordingly else we get the output as invalid choice