select = open("README.md")
for line in select:
     line = line.rstrip()
     if not line.startswith("Python: "):
          continue
     print(line)
