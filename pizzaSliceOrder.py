# Open a file
fo = open("b_small.in", "r");
print(fo.name);
fileLines=fo.readlines()
maxSlice = fileLines[0].split(" ")[0]
numberOfPizzaType = int(fileLines[0].split(" ")[1])
print("Maximum slice: ", maxSlice)
print("Number of Pizza Type: ", numberOfPizzaType)



pizzaSliceMap = fileLines[1].split(" ")
print("Pizza slice map: ", pizzaSliceMap)
print("Pizza slice map size: ", len(pizzaSliceMap))

maxPizzaSliceOrder = pizzaSliceMap[numberOfPizzaType-1]
print("Order count: ", maxPizzaSliceOrder)