print("------- Robotic command Using For Python -------")
print("\n---- Using avaliable command ----")
print("1.Start")
print("2.forward move")
print("3.backword move")
print("4.left move")
print("5.right move")
print("6.avoid the obstical")
print("7.stop")
print("8.exit")

while True:
     command = input("Enter the command: ").lower()
     if command == 'start':
          print("The robot start Moving.")
     elif command == 'forward move':
          print("The robot Forward Move.")
     elif command == 'backword move':
          print("The robot Backward Move.")
     elif command == 'left move':
          print("The robot Left Move.")
     elif command == 'right move':
          print("The robot Right Move.")
     elif command == 'avoid the obstical':
          print("The robot Avoid the obstical Move and reverse.")
     elif command == 'stop':
          print("The robot has Stop")
     elif command == 'exit':
          print("Thank You for using the Robotic command lines.")
          break
     else:
          print("invalid Command .Please enter correct command.")

