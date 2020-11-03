length = int(input("Please enter the number of unique keys:"))
dictionary = {}
valList = []

for i in range(length):

    keys = input("Please enter the key input value: ")
    valLength = int(input("Please enter the number of values for this specific key: "))
    valList = []
    for j in range(valLength):
        values = input("Please enter the value of the key: ")
        valList.append(values)
        dictionary[keys] = valList

    
print(dictionary)