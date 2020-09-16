x = input("Enter The Number: ")
try : x = int(x)
except :
    print("Enter a Valid Number")
    quit()
fact = 1
for i in range(x):
    if i==0: continue
    fact = fact * i
fact = fact * x
print("Factorial is:",fact)

print('Thus Factorial')
