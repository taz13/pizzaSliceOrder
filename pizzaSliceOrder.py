# Open a file
inputFile = open("e_also_big.in", "r");

fileLines = inputFile.readlines()
maxSlice = int(fileLines[0].split(" ")[0])
numberOfPizzaType = int(fileLines[0].split(" ")[1])

print("Maximum slice: ", maxSlice)
print("Number of Pizza Type: ", numberOfPizzaType)

pizzaSliceMap = fileLines[1].split(" ")
print("Pizza slice map: ", pizzaSliceMap)
print("Pizza slice map size: ", len(pizzaSliceMap))

countPizzaSliceOrder = int(pizzaSliceMap[numberOfPizzaType - 1])
pizzaTypeCount = 1;
pizzaSliceIndex = []
pizzaSliceIndex.append(numberOfPizzaType - 1)
index = numberOfPizzaType - 1;
remainingSlices = int(maxSlice) - countPizzaSliceOrder

#For finding the index of the next pizza type
def findNextIndex(endIndex):
    resultIndex = -1
    while int(pizzaSliceMap[endIndex]) > remainingSlices:
        endIndex = endIndex - 1
        if endIndex < 0:
            break;
    resultIndex = endIndex
    return resultIndex

#Loops through the pizza slice map and adds the pizza slice count
while countPizzaSliceOrder < maxSlice:
    pizzaSliceIndex = pizzaSliceIndex
    endIndex = index - 1;
    index = findNextIndex(endIndex);

    if index < 0:
        break
    else:
        pizzaSliceIndex.append(index)
        countPizzaSliceOrder = countPizzaSliceOrder + int(pizzaSliceMap[index])
        pizzaTypeCount = pizzaTypeCount + 1
        remainingSlices = maxSlice - countPizzaSliceOrder

print(pizzaTypeCount)
print(pizzaSliceIndex)

f = open("e_also_big_result.txt", "a")
f.writelines(str(pizzaTypeCount)+"\n")

indexCount = len(pizzaSliceIndex) - 1
while(indexCount>=0):
    f.write(str(pizzaSliceIndex[indexCount]) + " ")
    indexCount = indexCount - 1
f.close()