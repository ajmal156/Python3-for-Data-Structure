user = input(str("Enter the file name : "))
fname = open(user )

for line in fname:
     line = line.rstrip()
     print(line.upper())
