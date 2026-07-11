xfile = open("README.md")
count = 0
for line in xfile:
     count = count +1
print("Line count: " , count)
xfile.close()