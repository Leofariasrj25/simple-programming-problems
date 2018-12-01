def add_from_one_to(n):
	 return n * (n + 1)/2	
	
def multiply_from_one_to(n):
	product = 1	

	for i in range(1, n+1):
		product *= i

	return product

print("Welcome to sum-or-product v3000")
print("enter the number: ")
n = int(input("> "))
 
print(f"Press 1 to add all the numbers from 1 to {n}")
print(f"Press 2 to multiply all the numbers from 1 to {n}")
decision = int(input("> "))

if decision == 1:
	result = add_from_one_to(n)
	print(f"The sum of all numbers from 1 to {n} is {result}")

elif decision == 2:
	result = multiply_from_one_to(n)
	print(f"The product of all numbers from 1 to {n} is {result}")
