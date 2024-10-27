

tableNumber = int(input("Enter the number of which wnat table: "))
tableRange = int(input(f"Enter range for table of {tableNumber}: "))


def makeTableofNumber():
    
    for i in range(1 , tableRange + 1):
        print(f"{tableNumber} x {i} = {tableNumber * i}")

makeTableofNumber()