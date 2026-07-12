filename = input("Enter the file name: ")

file = open(filename)

data = file.read()
words = data.split()
words.sort()

unique_word = []

for word in words:
     if word not in unique_word:
          unique_word.append(word)

print(unique_word)

