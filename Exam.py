import random
myTable = [15,24,36,47,11]
varTemp = 0
varMax = 0


#1/ Permuter la case deux et trois
varTemp = myTable[2]
myTable[2] = myTable[1]
myTable[1] = varTemp

#2/ 
for i in range (len(myTable)):
    if (myTable[i]>varMax):
        varMax=myTable[i]
        myTable.append(myTable[3])



        



        print(varMax)

#4/




print(myTable)