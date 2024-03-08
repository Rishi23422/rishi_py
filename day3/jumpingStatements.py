# break, continue

for i in range(1,10):
    if i==5:
        break
    print(i)

print("Program exited")

for i in range(1,10):
    if i==5 or i==3 or i==7:
        continue
    print(i)

print("Printed all numbers between 1 to 10 except 5, 3 and 7")

for i in range(3,7,2):
    print(i)