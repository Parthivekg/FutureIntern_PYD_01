print("Press 1 to Add")
print("Press 2 to substract")
print("Press 3 to multiply")
print("Press 4 to divide")
option = int(input("choose an option:"))

if(option in [1,2,3,4]):
  num1 = int(input("Enter the first number:"))
  num2 = int(input("Enter the second number:"))
  if (option == 1):
      result = num1 + num2
  elif(option == 2):
      result = num1-num2 
  elif(option == 3):
      result = num1*num2
  else:
      result = num1//num2
else:
    print("Invalid opertaion selected")

print("The result of the operation is {}".format(result))