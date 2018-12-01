print("We're going to print the sum of multiples of 3 and 5 for a provided n")
n = int(input("Inform n: "))
sum = 0

# range is 0 based so we add 1 to include n
for i in range(3, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
        
