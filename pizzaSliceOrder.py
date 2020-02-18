# Open a file
inputFile = open("b_small.in", "r");
print(inputFile.name);
fileLines = inputFile.readlines()
maxSlice = int(fileLines[0].split(" ")[0])
numberOfPizzaType = int(fileLines[0].split(" ")[1])
print("Maximum slice: ", maxSlice)
print("Number of Pizza Type: ", numberOfPizzaType)

pizzaSliceMap = fileLines[1].split(" ")
print("Pizza slice map: ", pizzaSliceMap)
print("Pizza slice map size: ", len(pizzaSliceMap))

countPizzaSliceOrder = int(pizzaSliceMap[numberOfPizzaType - 1])

index = numberOfPizzaType - 2;
remainingSlices = int(maxSlice)


def findNextIndex(endIndex):
    while ()


while countPizzaSliceOrder < maxSlice:
    index = findNextIndex(index);
    countPizzaSliceOrder = countPizzaSliceOrder + pizzaSliceMap[index];
    print("Order count: ", findNextIndex(4))
    if index <= 0:
        break
    
print("Order count: ", countPizzaSliceOrder)
