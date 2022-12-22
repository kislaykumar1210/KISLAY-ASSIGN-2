num1 = float(input("Enter the First Number"))
num2 = float(input("Enter the Second Number"))
num3 = float(input("Enter the Third Number"))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

print("Or we can simply use a max() function to compare these numbers.")
print("The Largest number is", max(num2,num1,num3))
