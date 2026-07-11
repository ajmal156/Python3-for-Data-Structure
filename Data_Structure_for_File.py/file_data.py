fname = input("Enter the file name: ")
file = open(fname)

count = 0
total = 0.0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")          # Find the colon
        number = line[pos + 1:]       # Get everything after the colon
        value = float(number)         # Convert string to float
        total += value
        count += 1

average = total / count

print("Average spam confidence:", average)
