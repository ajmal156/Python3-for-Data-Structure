generlist = list()
while True:
     inp = input("Enter the number: ")
     if inp =='done':
          break

     value = float(inp)
     generlist.append(value)

averge =  sum(generlist) / len(generlist)

print("The average number is : ",averge)

